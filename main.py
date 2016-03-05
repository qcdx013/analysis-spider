# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from analysis_spider.spiders.autohome_price import AutohomePriceSpider

# fix error on amazon aws ec2
from scrapy import optional_features

try:
    optional_features.remove('boto')
except:
    # ignore
    print 'remove boto failed.'

process = CrawlerProcess(get_project_settings())

process.crawl(AutohomePriceSpider)
process.start()  # the script will block here until the crawling is finished
