# -*- coding: utf-8 -*-

from pybloom import BloomFilter
from scrapy.dupefilters import BaseDupeFilter
from scrapy.utils.job import job_dir


class BloomDupeFilter(BaseDupeFilter):
    def __init__(self, path=None):
        self.file = path
        self.fingerprints = BloomFilter(5000000, 0.00001)

    @classmethod
    def from_settings(cls, settings):
        return cls(job_dir(settings))

    def request_seen(self, request):
        if request.url in self.fingerprints:
            return True
        self.fingerprints.add(request.url)

    def close(self, reason):
        self.fingerprints = None
