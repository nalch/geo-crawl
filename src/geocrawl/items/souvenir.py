import scrapy

from .mixins import LastUpdatedMixin


class Souvenir(LastUpdatedMixin):
    image_url = scrapy.Field()
    title = scrapy.Field()
    aquired_on = scrapy.Field()
