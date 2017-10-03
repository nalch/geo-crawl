# geo-crawl
geocrawl is a utility for getting information about your geocaches from geocaching.com. As geocaching.com does not accept API access anymore and the API is borderline not usable for non-premium users this crawler provides third-party applications with their database.

## Usage

### Configuration
The scraping of caches is done with the according account, so the credentials have to be provided. This happens via the environment variables `GC_USERNAME` and `GC_PASSWORD`.

### Running
All spiders have shortcut functions for easy execution. You can pass handlers for every signal specified in scrapy's signal module.
```
from geocrawl.runner import get_all, print_item_title
get_all(on_item_scraped=print_item_title)
```

```
from geocrawl.runner import get_short_caches, print_item_title
get_short_caches(on_item_scraped=print_item_title)
```

## Development
* Clone the repository
* Change the .environment file or set the environment variables
  * GC_USERNAME
  * GC_PASSWORD
  * SCRAPY_SETTINGS_MODULE