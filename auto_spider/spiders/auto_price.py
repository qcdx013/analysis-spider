# -*- coding: utf-8 -*-

import json

import requests
import scrapy
from scrapy.spiders import CrawlSpider

from ..items import CarPriceItem, CityItem, SpecItem


class AutohomePriceSpider(CrawlSpider):
    name = 'autohome-price'
    allowed_domains = ['223.99.255.20']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
        'Host': '223.99.255.20',
    }

    session = requests.Session()
    session.headers.update(headers)

    # 从起始url获取全部汽车品牌
    def start_requests(self):
        url = 'http://223.99.255.20/app.api.autohome.com.cn/autov5.4.0/news/province-pm2-ts0.json'
        yield scrapy.Request(url, callback=self.parse_citys)

    # 获取所有城市信息
    def parse_citys(self, response):
        provinces = json.loads(response.body_as_unicode())['result']['provinces']
        city_list = []

        for province in provinces:
            for city in province['citys']:
                city_list.append(city)
                # sometimes we needn't parse city items
                # yield self.parse_item_city(city, province)

        url = 'http://223.99.255.20/app.api.autohome.com.cn/autov5.4.0/cars/brands-pm2-ts0.json'

        # 获取所有品牌
        yield scrapy.Request(url, callback=self.parse_brands, meta={'citys': city_list})

    @staticmethod
    def parse_item_city(city, province):
        i = CityItem()
        i['province_id'] = province['id']
        i['province_name'] = province['name']
        i['province_first_letter'] = province['firstletter']
        i['city_id'] = city['id']
        i['city_name'] = city['name']
        i['city_first_letter'] = city['firstletter']
        return i

    # 根据汽车品牌获取全部汽车型号
    def parse_brands(self, response):
        meta = response.meta
        brands = json.loads(response.body_as_unicode())['result']['brandlist']

        for brand in brands:
            brand_first_letter = brand['letter']
            bnd_list = brand['list']

            for bnd in bnd_list:
                url = 'http://223.99.255.20/app.api.autohome.com.cn/autov5.4.0/cars/seriesprice-pm2-b{0}-t2.json'.format(
                        bnd['id'])
                meta.update({'brand_id': bnd['id'], 'brand_name': bnd['name'],
                             'brand_first_letter': brand_first_letter, 'brand_img_url': bnd['imgurl']})

                # 获取全部车型
                yield scrapy.Request(url, callback=self.parse_series, meta=meta)

    # 根据汽车型号获取全部城市的详情
    def parse_series(self, response):
        fcts = json.loads(response.body_as_unicode())['result']['fctlist']

        for fct in fcts:
            fct_name = fct['name']
            series = fct['serieslist']

            for sis in series:
                meta = response.meta
                meta.update({'fct_name': fct_name, 'series_id': sis['id'],
                             'series_name': sis['name'], 'series_img_url': sis['imgurl']})

                # 遍历所有城市，获取该型号汽车详情
                for city in meta['citys']:
                    meta.update({'city_id': city['id']})
                    url = 'http://223.99.255.20/app.api.autohome.com.cn/autov5.4.0/cars/' \
                          'seriessummary-pm2-s{0}-t0x000c-c{1}.json'.format(sis['id'], city['id'])
                    yield scrapy.Request(url, callback=self.parse_series_detail, meta=meta)

    # 根据汽车详情页获取报价
    def parse_series_detail(self, response):
        meta = response.meta

        # 遍历所有型号，获取报价
        engines = json.loads(response.body_as_unicode())['result']['enginelist']

        for engine in engines:
            specs = engine['speclist']

            for spec in specs:
                yield self.parse_item_price(meta, spec)
                # sometimes we needn't parse spec items
                # yield self.parse_item_spec(meta, spec)

    @staticmethod
    def parse_item_spec(meta, spec):
        si = SpecItem()
        si['brand_id'] = meta['brand_id']
        si['brand_name'] = meta['brand_name']
        si['brand_first_letter'] = meta['brand_first_letter']
        si['brand_img_url'] = meta['brand_img_url']
        si['fct_name'] = meta['fct_name']
        si['series_id'] = meta['series_id']
        si['series_name'] = meta['series_name']
        si['series_img_url'] = meta['series_img_url']
        si['spec_id'] = spec['id']
        si['spec_name'] = spec['name']
        return si

    @staticmethod
    def parse_item_price(meta, spec):
        i = CarPriceItem()
        i['spec_id'] = spec['id']
        i['city_id'] = meta['city_id']
        i['price'] = spec['price']
        i['price_min'] = spec['minprice']
        return i
