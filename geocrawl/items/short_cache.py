import scrapy

from .mixins import LastUpdatedMixin


class ShortCache(LastUpdatedMixin):
    log_type = scrapy.Field()
    found_date = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    region = scrapy.Field()
    country = scrapy.Field()
    detail_link = scrapy.Field()
