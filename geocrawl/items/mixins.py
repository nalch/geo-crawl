import scrapy

from .loaders import datetime_serializer


class LastUpdatedMixin(scrapy.Item):
    last_updated = scrapy.Field(serializer=datetime_serializer)
