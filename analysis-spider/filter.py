# -*- coding: utf-8 -*-

from pybloom import BloomFilter
from scrapy.utils.job import job_dir
from scrapy.dupefilters import BaseDupeFilter

FILE_PATH = 'bloom.data'


class BloomDupeFilter(BaseDupeFilter):
    def __init__(self, path=None):
        self.file = FILE_PATH
        self.fingerprints = BloomFilter(5000000, 0.00001)

    @classmethod
    def from_settings(cls, settings):
        return cls(job_dir(settings))

    def request_seen(self, request):
        fp = request.url
        if fp in self.fingerprints:
            return True
        self.fingerprints.add(fp)

    def close(self, reason):
        self.fingerprints = None
