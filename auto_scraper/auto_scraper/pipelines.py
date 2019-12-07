import logging
import os
import csv
import datetime
from collections import OrderedDict

from auto_scraper.items import Paragraph


def create_ad_dict(class_object):
    return OrderedDict(sorted(vars(class_object)['fields'].items(), key=lambda t: t[0]))


def create_ordered_item(item):
    return OrderedDict(sorted(item.items(), key=lambda t: t[0]))


class CsvWriterPipeline(object):
    filename, file, writer = -1, -1, -1

    def open_spider(self, spider):
        self.filename = "result.csv"
        logging.info(f"Saving results to {self.filename}.")
        self.file = open(self.filename, 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file, delimiter='|')
        dictionary = create_ad_dict(Paragraph)
        header = [key for key in dictionary.keys()]
        print(header)
        self.writer.writerow(header)

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, _):
        dictionary = create_ordered_item(item)
        values = [value for value in dictionary.values()]
        self.writer.writerow(values)
