# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re

from pybloom import BloomFilter

from items import CarPriceItem, SpecItem, CityItem
from model.auto_price import CarPrice, Spec, City, Base
from model.config import DBSession, engine

# 缓冲区大小，批量插入数据库
BUF = 100000


# 存储到数据库
class PriceDataBasePipeline(object):
    def __init__(self):
        self.session = DBSession()
        self.count = BUF

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if not isinstance(item, CarPriceItem):
            return item

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
            self.count = BUF

        return item

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()


class CityDataBasePipeline(object):
    def __init__(self):
        self.session = DBSession()
        self.count = BUF

    def open_spider(self, spider):
        Base.metadata.tables[City.__tablename__].create(checkfirst=True)
        conn = engine.connect()
        conn.execute(
                'ALTER TABLE {0} CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci'.format(
                        City.__tablename__))
        conn.execute('TRUNCATE TABLE {0}'.format(City.__tablename__))

    def process_item(self, item, spider):
        if not isinstance(item, CityItem):
            return item

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
            self.count = BUF

        return item

    def close_spider(self, spider):
        self.session.commit()

        if self.session.query(City).count() > 0:
            # rename tables
            conn = engine.connect()
            conn.execute(
                    'RENAME TABLE t_citys TO t_citys_000, {0} TO t_citys, t_citys_000 TO {0}'.format(
                            City.__tablename__))


class SpecDataBasePipeline(object):
    def __init__(self):
        self.fingerprints = BloomFilter(10000, 0.00001)
        self.session = DBSession()
        self.count = BUF

    def open_spider(self, spider):
        Base.metadata.tables[Spec.__tablename__].create(checkfirst=True)
        conn = engine.connect()
        conn.execute(
                'ALTER TABLE {0} CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci'.format(
                        Spec.__tablename__))
        conn.execute('TRUNCATE TABLE {0}'.format(Spec.__tablename__))

    def process_item(self, item, spider):
        if not isinstance(item, SpecItem):
            return item

        if item['spec_id'] in self.fingerprints:
            # duplicate
            return item

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

        self.fingerprints.add(item['spec_id'])

        self.session.add(s)
        self.count -= 1

        if self.count <= 0:
            self.session.commit()
            self.count = BUF

        return item

    def close_spider(self, spider):
        self.session.commit()

        if self.session.query(Spec).count() > 0:
            # rename tables
            conn = engine.connect()
            conn.execute(
                    'RENAME TABLE t_specs TO t_specs_000, {0} TO t_specs, t_specs_000 TO {0}'.format(
                            Spec.__tablename__))

        self.fingerprints = None
