import scrapy

from .mixins import LastUpdatedMixin


class Geocache(LastUpdatedMixin):
    geocode = scrapy.Field()
    title = scrapy.Field()

    size = scrapy.Field()
    terrain = scrapy.Field()
    difficulty = scrapy.Field()
    owner = scrapy.Field()
    coordinates = scrapy.Field()
