# -*- coding: utf-8 -*-

from scrapy.dupefilters import BaseDupeFilter
from scrapy.utils.job import job_dir

from model.config import r


class BloomDupeFilter(BaseDupeFilter):
    def __init__(self, path=None):
        self.key = 'spider:price:bloom:url'
        self.path = path
        r.delete(self.key)  # 清空bloom

    @classmethod
    def from_settings(cls, settings):
        return cls(job_dir(settings))

    def request_seen(self, request):
        if r.pfadd(self.key, request.url) != 1:
            return True
