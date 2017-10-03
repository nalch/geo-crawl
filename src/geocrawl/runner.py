from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders.geo_spider import (
    GeocachingSpider,
    ShortGeocachingSpider
)


def print_item(item, response, spider):
    print(item)


def print_item_title(item, response, spider):
    print(item['title'])


def get_all(**kwargs):
    process = CrawlerProcess(get_project_settings())
    process.crawl(GeocachingSpider, **kwargs)
    process.start()


def get_short_caches(**kwargs):
    process = CrawlerProcess(get_project_settings())
    process.crawl(ShortGeocachingSpider, **kwargs)
    process.start()


if __name__ == '__main__':
    #get_all(on_item_scraped=print_item_title)
    get_short_caches(on_item_scraped=print_item_title)

