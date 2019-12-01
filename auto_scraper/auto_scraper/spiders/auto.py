# coding=utf-8
import datetime
import scrapy
import pytz
from scrapy import Spider, Request
from auto_scraper.utils import name_to_url_dict, websites

time_zone = pytz.timezone('Europe/Warsaw')
now = datetime.datetime.now(time_zone)
matching_days = [now, (now - datetime.timedelta(days=1)).date()]


def convert_to_url(string):
    return ''.join(name_to_url_dict.get(char, char) for char in string.lower())


class AutomatedWebSpider(Spider):
    name = "auto_scraper"
    allowed_domains = [site['domain'] for site in websites]
    start_urls = [site['url'] for site in websites]
    # start_urls = ['https://google.pl']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse(self, response: scrapy.http.Response):
        urls = response.xpath("//*/@href").extract()
        urls = [url for url in urls]
        paragrapghs = response.xpath("//*[self::a or self::p]/text()").extract()
        paragrapghs = filter(lambda x: len(x) > 60, paragrapghs)
        paragrapghs = [par.strip().replace('\n', '') for par in paragrapghs]
        # print(urls)
        for par in paragrapghs:
            print(response.url, par)
        for url in urls:
            if url[0] == '/':
                base_url_end = 10 + response.url[10:].find('/')
                base_url = response.url[:base_url_end]
                print("BASE", base_url, response.url, base_url_end, url)
                url = base_url + url
            try:
                request = Request(url, callback=self.parse)
                request.meta['url'] = url
                yield request
            except ValueError:
                print(f"Wrong url: {url}")






