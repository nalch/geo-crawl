import scrapy

from .mixins import LastUpdatedMixin


class Souvenir(LastUpdatedMixin):
    title = scrapy.Field()

    by = scrapy.Field()
    artist = scrapy.Field()
    about_artist = scrapy.Field()
    additional_information = scrapy.Field()
    image = scrapy.Field()
