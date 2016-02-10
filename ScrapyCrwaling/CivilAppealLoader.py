from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join

import sys

from ScrapyCrwaling import CivilAppeal

reload(sys)
sys.setdefaultencoding('utf-8')


def test(str):
    print str
    return str


class CivilAppealLoader(ItemLoader):
    default_item_class = CivilAppeal
    default_output_processor = TakeFirst()
    default_input_processor = MapCompose(lambda string: string.encode('utf-8'))
    # default_input_processor = MapCompose(test)