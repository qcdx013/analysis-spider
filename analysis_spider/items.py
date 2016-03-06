# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarPriceItem(scrapy.Item):
    spec_id = scrapy.Field()
    city_id = scrapy.Field()
    price = scrapy.Field()
    price_min = scrapy.Field()


class SpecItem(scrapy.Item):
    brand_id = scrapy.Field()
    brand_name = scrapy.Field()
    brand_first_letter = scrapy.Field()
    brand_img_url = scrapy.Field()
    fct_name = scrapy.Field()
    series_id = scrapy.Field()
    series_name = scrapy.Field()
    series_img_url = scrapy.Field()
    spec_id = scrapy.Field()
    spec_name = scrapy.Field()


class CityItem(scrapy.Item):
    province_id = scrapy.Field()
    province_name = scrapy.Field()
    province_first_letter = scrapy.Field()
    city_id = scrapy.Field()
    city_name = scrapy.Field()
    city_first_letter = scrapy.Field()
