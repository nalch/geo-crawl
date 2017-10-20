from distutils.core import setup

VERSION = '0.1'

setup(
    name='geocrawl',
    packages=['geocrawl'],
    version=VERSION,
    license='MIT',
    description='A library to stream geocaching related entities from the official website',
    author='Kristian Scholze',
    url='https://github.com/nalch/geo-crawl',
    download_url='https://github.com/nalch/geo-crawl/archive/{}.tar.gz'.format(VERSION),
    keywords=['scrapy', 'geocaching', 'cache'],
    classifiers=[],
)
