from datetime import datetime

from scrapy import (
    FormRequest,
    Spider,
    signals
)

from geocrawl.items import (
    Geocache,
    ShortCache
)
from geocrawl.items.loaders import TextValueLoader

from geocrawl.urls import STARTURL

from geocrawl.xpath_mappings import (
    GEOCACHE_MAPPING,
    SHORTCACHE_MAPPING
)

SIGNAL_NAMES = [var for var in vars(signals) if not var.startswith('_')]


class GeoLoginSpider(Spider):
    start_urls = [STARTURL]

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(GeoLoginSpider, cls).from_crawler(crawler, *args, **kwargs)
        try:
            passed_signal_handler = filter(lambda sn: 'on_{}'.format(sn) in kwargs.keys(), SIGNAL_NAMES)
            for signame in passed_signal_handler:
                crawler.signals.connect(kwargs['on_{}'.format(signame)], signal=getattr(signals, signame))
        except KeyError:
            pass
        return spider

    def parse(self, response):
        username = self.settings.attributes['GC_USERNAME'].value
        password = self.settings.attributes['GC_PASSWORD'].value
        return FormRequest.from_response(
            response,
            formdata={
                'Username': username,
                'Password': password
            },
            callback=self.process_login_response
        )

    def process_login_response(self, response):
        pass


class ShortGeocachingSpider(GeoLoginSpider):
    name = 'short_geocaching_spider'

    def process_login_response(self, response):
        for row in response.css('#divContentMain table.Table tr'):
            yield self.parse_short_cache(row)

    def parse_short_cache(self, row):
        sc_item = TextValueLoader(item=ShortCache(), selector=row)
        for field, xpath_selector in SHORTCACHE_MAPPING.items():
            sc_item.add_xpath(field, xpath_selector)

        sc_item.add_value('last_updated', datetime.now())
        return sc_item.load_item()


class GeocachingSpider(ShortGeocachingSpider):
    name = 'geocaching_spider'

    def process_login_response(self, response):
        for short_cache in super(GeocachingSpider, self).process_login_response(response):
            yield response.follow(short_cache['detail_link'], self.parse_cache_details)

    def parse_cache_details(self, response):
        gc_item = TextValueLoader(item=Geocache(), selector=response)
        for field, xpath_selector in GEOCACHE_MAPPING.items():
            gc_item.add_xpath(field, xpath_selector)

        gc_item.add_value('last_updated', datetime.now())
        return gc_item.load_item()
