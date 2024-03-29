# -*- coding: utf-8 -*-

import datetime

from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

# 初始化数据库连接
engine = create_engine('mysql+mysqldb://user:pwd@mysql:3306/db', encoding='utf-8')

engine.execute('SET NAMES utf8mb4')
engine.execute('SET CHARACTER SET utf8mb4')
engine.execute('SET character_set_connection=utf8mb4')

metadata = MetaData(bind=engine)

Base = declarative_base(metadata=metadata)


class CarPrice(Base):
    __tablename__ = 'autohome_car_price'

    spec_id = Column(String(64), primary_key=True)
    city_id = Column(String(64), primary_key=True)
    price = Column(Float)
    price_min = Column(Float)
    datetime = Column(DateTime, default=datetime.datetime.now(), primary_key=True)


class Spec(Base):
    __tablename__ = 't_specs_backup'

    brand_id = Column(String(64))
    brand_name = Column(String(255))
    brand_first_letter = Column(String(8))
    brand_img_url = Column(String(255))
    fct_name = Column(String(255))
    series_id = Column(String(64))
    series_name = Column(String(255))
    series_img_url = Column(String(255))
    spec_id = Column(String(64), primary_key=True)
    spec_name = Column(String(255))


class City(Base):
    __tablename__ = 't_citys_backup'

    province_id = Column(String(64))
    province_name = Column(String(64))
    province_first_letter = Column(String(8))
    city_id = Column(String(64), primary_key=True)
    city_name = Column(String(64))
    city_first_letter = Column(String(8))
