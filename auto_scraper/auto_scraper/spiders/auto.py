# coding=utf-8
import datetime
import scrapy
import logging
import pytz
from scrapy import Spider, Request
from scrapy.utils.log import configure_logging

from auto_scraper.utils import name_to_url_dict, websites
from auto_scraper.items import Paragraph

time_zone = pytz.timezone('Europe/Warsaw')
now = datetime.datetime.now(time_zone)
date = datetime.date.today().strftime('%Y%m%d')


def convert_to_url(string):
    return ''.join(name_to_url_dict.get(char, char) for char in string.lower())


class AutomatedWebSpider(Spider):
    name = "auto_scraper"
    allowed_domains = [site['domain'] for site in websites]
    start_urls = [site['url'] for site in websites]
    # start_urls = ['https://google.pl']

    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='log.txt',
        format='%(levelname)s: %(message)s',
        level=logging.DEBUG
    )

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse(self, response: scrapy.http.Response):
        if response.url[-4:] in ['.css', 'json']:
            return
        urls = response.xpath("//*/@href").extract()
        urls = [url for url in urls]
        paragrapghs = response.xpath("//*[self::a or self::p]/text()").extract()
        paragrapghs = filter(lambda x: len(x) > 120, paragrapghs)
        paragrapghs = [par.strip().replace('\n', '') for par in paragrapghs]
        # print(urls)
        for par in paragrapghs:
            print(response.url, par)
            item = Paragraph()
            item['date'] = date
            item['category'] = 'restaurants'
            item['lang'] = 'EN'
            item['site'] = response.url.split('://')[1].split('/')[0]
            item['text'] = par.replace('"', '').replace("'", "")
            item['source_url'] = response.url
            yield item
        for url in filter(lambda x: x and len(x) > 0, urls):
            if url[0] == '/':
                base_url_end = 10 + response.url[10:].find('/')
                base_url = response.url[:base_url_end]
                # print("BASE", base_url, response.url, base_url_end, url)
                url = base_url + url
            try:
                request = Request(url, callback=self.parse)
                request.meta['url'] = url
                yield request
            except ValueError:
                print(f"Wrong url: {url}")






