SHORTCACHE_MAPPING = {
    'log_type': './td[1]/img[1]/attribute::title',
    'found_date': './td[3]/text()',
    'type': './td[4]//a[1]/img[1]/attribute::title',
    'title': './td[4]//a[2]//text()',
    'region': './td[5]//text()',
    'detail_link': './td[4]//a[1]/attribute::href'
}

GEOCACHE_MAPPING = {
    'geocode': '//*[@id="ctl00_ContentBody_CoordInfoLinkControl1_uxCoordInfoCode"]//text()',
    'title': '//*[@id="ctl00_ContentBody_CacheName"]//text()',
    'owner': '//*[@id="ctl00_ContentBody_mcd1"]/a//text()',
    'difficulty': '//*[@id="ctl00_ContentBody_uxLegendScale"]/img/attribute::src',
    'terrain': '//*[@id="ctl00_ContentBody_Localize12"]/img/attribute::src',
    'size': '//*[@id="ctl00_ContentBody_size"]/p/span/img/attribute::src',
    'coordinates': '//*[@id="uxLatLon"]//text()'
}