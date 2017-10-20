import os
import re

from datetime import (
    date,
    datetime
)

from scrapy.loader import ItemLoader
from scrapy.loader.processors import (
    Compose,
    TakeFirst
)

SOUVENIR_REGEX = re.compile(r'\D*\s(\d{2}/\d{2}/\d{4})')


def value_strip(value):
    if not isinstance(value, str):
        return value
    return value.strip()


def datetime_serializer(value):
    if not isinstance(value, (datetime, date)):
        return value

    return value.isoformat()


def value_from_filename(value):
    return os.path.splitext(os.path.basename(value))[0]


def starrating_from_filename(value):
    return float(value_from_filename(value).replace('stars', '').replace('_', '.'))


def aquired_on_serializer(value):
    return datetime.strptime(
        SOUVENIR_REGEX.match(value).group(1), '%m/%d/%Y'
    ).isoformat()


class TextValueLoader(ItemLoader):
    default_output_processor = Compose(TakeFirst().__call__, value_strip)

    size_in = Compose(TakeFirst().__call__, value_from_filename)
    difficulty_in = Compose(TakeFirst().__call__, starrating_from_filename)
    terrain_in = Compose(TakeFirst().__call__, starrating_from_filename)

    aquired_on_in = Compose(TakeFirst().__call__, aquired_on_serializer)
