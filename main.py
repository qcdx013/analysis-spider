# -*- coding: utf-8 -*-
import requests
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from auto_spider.spiders.auto_price import AutohomePriceSpider

process = CrawlerProcess(get_project_settings())

process.crawl(AutohomePriceSpider)

# send notify
requests.get(
        'http://sc.ftqq.com/SCU789T8aa9cb97fe91104109a998fed9dfab48567804bb52076.send?text=Analysis-spider-is-working!...')

process.start()  # the script will block here until the crawling is finished
