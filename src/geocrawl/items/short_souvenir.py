import scrapy

from .mixins import LastUpdatedMixin


class ShortSouvenir(LastUpdatedMixin):
    image_url = scrapy.Field()
    title = scrapy.Field()
    aquired_on = scrapy.Field()
    detail_link = scrapy.Field()
