# geo-crawl ![Build status](https://travis-ci.org/nalch/geo-crawl.svg?branch=master)
geocrawl is a utility for getting information about your geocaches from geocaching.com. As geocaching.com does not accept API access anymore and the API is borderline not usable for non-premium users this crawler provides third-party applications with their database.

## Usage

### Configuration
The scraping of caches is done with the according account, so the credentials have to be provided. This happens via the environment variables `GC_USERNAME` and `GC_PASSWORD`.
If running the shortcut functions use the keyword arguments `username` and `password`.

### Running
All spiders have shortcut functions for easy execution. You can pass handlers for every signal specified in scrapy's signal module.
```
from geocrawl.runner import get_all, print_item_title
get_all(username='<username>', password='<password>', on_item_scraped=print_item_title)
```

### Available shortcuts

#### get_all
```
{ 
  'archived': '1',
  'coordinates': 'N 51° 02.490 E 013° 48.018',
  'difficulty': 3.0,
  'geocode': 'GC210CN',
  'last_updated': '2017-10-21T20:31:46.000095',
  'owner': 'Ulvieh',
  'size': 'other',
  'terrain': 1.0,
  'title': 'Raucher sterben früher'
}
```
#### get_short_caches
```
{ 
  'detail_link': 'https://www.geocaching.com/seek/cache_details.aspx?guid=ea58e320-77ac-44b4-9dd5-289daa67c64c',
  'found_date': '07/30/2014',
  'last_updated': '2017-10-21T20:30:34.017642',
  'log_type': 'Found it',
  'region': 'Sachsen, Germany',
  'title': 'Raucher sterben früher',
  'type': 'Traditional Cache'
}
```

#### get_short_souvenirs
```
{
  'aquired_on': '2014-07-30T00:00:00',
  'detail_link': '/souvenir/?guid=728b71b1-ffea-4a3b-b606-94596e62a8c6',
  'image_url': 'https://souvenirs.geocaching.com/SouvenirImages/NC82LzIwMTc/130ee86a-bb8c-4be3-8df4-b36bc1d88c19.png',
  'last_updated': '2017-10-21T20:32:39.542409',
  'title': 'Deutschland'
}
```

#### get_souvenirs
```
{
  'about_artist': 'Hillary E. is a Groundspeak Lackey with a passion for '
                  'nature. She loves birdwatching, backpacking, and travel, but '
                  'above all she loves to make art. Her goals in life include '
                  'building animatronic dinosaurs and taming ostriches.',
  'additional_information': 'Der Freistaat Sachsen ist die Heimat von einigen '
                            'der größten Ringgrabenanlagen in Europa, die '
                            'teilweise aus dem fünften Jahrhundert v. Chr. '
                            'stammen. Es ist seit dem ersten Jahrhundert v. '
                            'Chr. die Heimat des Germanischen Volkes. Napoleon '
                            'machte Sachsen zu einem selbständigen Königreich. '
                            'Es blieb selbstständig, bis es gezwungen wurde, '
                            'dem Norddeutschen Bund beizutreten.',
  'artist': 'Hillary E.',
  'image': 'https://souvenirs.geocaching.com/SouvenirImages/MTIvMjMvMjAxMA/0a41c3c6-9d63-4755-90f6-13d411657a49.png',
  'last_updated': '2017-10-21T20:33:36.839568',
  'title': 'Sachsen'}
```

## Development
* Clone the repository
* Change the .environment file or set the environment variables
  * GC_USERNAME
  * GC_PASSWORD
  * SCRAPY_SETTINGS_MODULE