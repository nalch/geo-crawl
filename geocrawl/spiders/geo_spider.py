from datetime import datetime

from scrapy import (
    FormRequest,
    Spider,
    signals
)

from geocrawl.items import (
    Geocache,
    ShortCache,
    ShortSouvenir,
    Souvenir
)
from geocrawl.items.loaders import TextValueLoader

from geocrawl.urls import (
    LOGS_URL,
    SOUVENIR_URL,
    STARTURL
)

from geocrawl.xpath_mappings import (
    GEOCACHE_MAPPING,
    SHORTCACHE_MAPPING,
    SOUVENIR_ENTRY,
    SHORT_SOUVENIR_MAPPING,
    SOUVENIR_MAPPING
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
        self.username = getattr(self, 'username', self.settings.attributes['GC_USERNAME'].value)
        self.password = getattr(self, 'password', self.settings.attributes['GC_PASSWORD'].value)
        return FormRequest.from_response(
            response,
            formdata={
                'Username': self.username,
                'Password': self.password
            },
            callback=self.process_login_response
        )

    def process_login_response(self, response):
        pass


class ShortGeocachingSpider(GeoLoginSpider):
    name = 'short_geocaching_spider'
    start_urls = ['{}{}'.format(STARTURL, LOGS_URL)]

    def process_login_response(self, response):
        for row in response.css('#divContentMain table.Table tr'):
            yield self.parse_short_cache(row)

    def parse_short_cache(self, row):
        sc_item = TextValueLoader(item=ShortCache(), selector=row)
        for field, xpath_selector in SHORTCACHE_MAPPING.items():
            sc_item.add_xpath(field, xpath_selector)

        sc_item.add_value('last_updated', datetime.now().isoformat())
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

        gc_item.add_value('last_updated', datetime.now().isoformat())
        return gc_item.load_item()


class ShortSouvenirGeocachingSpider(GeoLoginSpider):
    name = 'short_souvenir_geocaching_spider'
    start_urls = ['{}{}'.format(STARTURL, SOUVENIR_URL)]

    def process_login_response(self, response):
        for souvenir in response.xpath(SOUVENIR_ENTRY):
            sc_item = TextValueLoader(item=ShortSouvenir(), selector=souvenir)
            for field, xpath_selector in SHORT_SOUVENIR_MAPPING.items():
                sc_item.add_xpath(field, xpath_selector)

            sc_item.add_value('last_updated', datetime.now().isoformat())
            yield sc_item.load_item()


class SouvenirGeocachingSpider(ShortSouvenirGeocachingSpider):
    name = 'souvenir_geocaching_spider'

    def process_login_response(self, response):
        for short_souvenir in super(SouvenirGeocachingSpider, self).process_login_response(response):
            yield response.follow(short_souvenir['detail_link'], self.parse_souvenir_details)

    def parse_souvenir_details(self, response):
        souvenir_item = TextValueLoader(item=Souvenir(), selector=response)
        for field, xpath_selector in SOUVENIR_MAPPING.items():
            souvenir_item.add_xpath(field, xpath_selector)

        souvenir_item.add_value('last_updated', datetime.now().isoformat())
        return souvenir_item.load_item()
