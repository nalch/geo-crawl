from scrapy.crawler import CrawlerProcess

from spiders.geo_spider import (
    GeocachingSpider,
    ShortGeocachingSpider
)


def print_item(item, response, spider):
    print(item)


def print_item_title(item, response, spider):
    print(item['title'])


def get_all(**kwargs):
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(GeocachingSpider, **kwargs)
    process.start()


def get_short_caches(**kwargs):
    settings = {'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}
    process = CrawlerProcess(settings)

    process.crawl(ShortGeocachingSpider, **kwargs)
    process.start()


# get_all(on_item_scraped=print_item_title)
get_short_caches(on_item_scraped=print_item_title)

