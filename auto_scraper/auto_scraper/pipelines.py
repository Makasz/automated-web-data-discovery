import logging
import os
import datetime
from collections import OrderedDict

from auto_scraper.items import Advertisement


class CsvWriterPipeline(object):
    filename, file = -1, -1

    def open_spider(self, spider):
        self.filename = "result.json"
        logging.info(f"Saving results to {self.filename}.")
        self.file = open(self.filename, 'w', newline='', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, _):
        pass
