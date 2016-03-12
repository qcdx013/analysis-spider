# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re

from scrapy.exceptions import DropItem

from items import CarPriceItem, SpecItem, CityItem
from model.auto_price import CarPrice, Spec, City
from model.config import DBSession

from model.config import r

# 缓冲区大小，批量插入数据库
BUF_SIZE_000 = 5000


# 存储到数据库
class DataBasePipeline(object):
    def __init__(self):
        self.session = DBSession()
        self.count = BUF_SIZE_000

    def open_spider(self, spider):
        pass

    def process_item_city(self, item):
        c = City(
                province_id=item['province_id'],
                province_name=item['province_name'].encode('utf-8'),
                province_first_letter=item['province_first_letter'].encode('utf-8'),
                city_id=item['city_id'],
                city_name=item['city_name'].encode('utf-8'),
                city_first_letter=item['city_first_letter'].encode('utf-8'),
        )

        self.session.add(c)
        self.count -= 1

        if self.count <= 0:
            self.session.commit()
            self.count = BUF_SIZE_000

        return item

    def process_item_spec(self, item):
        s = Spec(
                brand_id=item['brand_id'],
                brand_name=item['brand_name'].encode('utf-8'),
                brand_first_letter=item['brand_first_letter'].encode('utf-8'),
                brand_img_url=item['brand_img_url'].encode('utf-8'),
                fct_name=item['fct_name'].encode('utf-8'),
                series_id=item['series_id'],
                series_name=item['series_name'].encode('utf-8'),
                series_img_url=item['series_img_url'].encode('utf-8'),
                spec_id=item['spec_id'],
                spec_name=item['spec_name'].encode('utf-8'),
        )

        self.session.add(s)
        self.count -= 1

        if self.count <= 0:
            self.session.commit()
            self.count = BUF_SIZE_000

        return item

    def process_item_car_price(self, item):
        price = item['price'].encode('utf-8')
        m = re.search(r'[0-9\.]+', price)
        price = m and float(m.group(0)) or 0.0

        price_min = item['price_min'].encode('utf-8')
        m = re.search(r'[0-9\.]+', price_min)
        price_min = m and float(m.group(0)) or 0.0

        c = CarPrice(
                spec_id=item['spec_id'],
                city_id=item['city_id'],
                price=price,
                price_min=price_min,
        )

        self.session.add(c)
        self.count -= 1

        if self.count <= 0:
            self.session.commit()
            self.count = BUF_SIZE_000

        return item

    def process_item(self, item, spider):
        if isinstance(item, SpecItem):
            return self.process_item_spec(item)
        elif isinstance(item, CarPriceItem):
            return self.process_item_car_price(item)
        elif isinstance(item, CityItem):
            return self.process_item_city(item)

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()


# 车型去重
class DuplicatesPipeline(object):
    def process_item(self, item, spider):
        if not isinstance(item, SpecItem):
            return item

        if r.hset('spider:auto:duplicate:spec', item['spec_id'], '') == 1:
            return item

        pass  # ignore
        # raise DropItem("Duplicate series found: {0}".format(sid))
