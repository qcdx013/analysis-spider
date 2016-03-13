# -*- coding: utf-8 -*-

import datetime

from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

from auto_spider.model.config import metadata

Base = declarative_base(metadata=metadata)


class CarPrice(Base):
    __tablename__ = 'autohome_car_price'

    spec_id = Column(String, primary_key=True)
    city_id = Column(String, primary_key=True)
    price = Column(Float)
    price_min = Column(Float)
    datetime = Column(DateTime, default=datetime.datetime.now(), primary_key=True)


class Spec(Base):
    __tablename__ = 't_specs_tmp'

    brand_id = Column(String)
    brand_name = Column(String)
    brand_first_letter = Column(String)
    brand_img_url = Column(String)
    fct_name = Column(String)
    series_id = Column(String)
    series_name = Column(String)
    series_img_url = Column(String)
    spec_id = Column(String, primary_key=True)
    spec_name = Column(String)


class City(Base):
    __tablename__ = 't_citys'

    province_id = Column(String)
    province_name = Column(String)
    province_first_letter = Column(String)
    city_id = Column(String, primary_key=True)
    city_name = Column(String)
    city_first_letter = Column(String)
