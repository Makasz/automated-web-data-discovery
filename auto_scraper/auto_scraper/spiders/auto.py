# coding=utf-8
import datetime
import pytz
import scrapy
from scrapy import Spider, Request
from auto_scraper.utils import name_to_url_dict, websites

time_zone = pytz.timezone('Europe/Warsaw')
now = datetime.datetime.now(time_zone)
matching_days = [now, (now - datetime.timedelta(days=1)).date()]


def convert_to_url(string):
    return ''.join(name_to_url_dict.get(char, char) for char in string.lower())


class AutomatedWebSpider(Spider):
    name = "auto_scraper"
    allowed_domains = ["londoneater.com"]
    start_urls = [site['url'] for site in websites]
    # start_urls = ['https://google.pl']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse(self, response: scrapy.http.Response):
        url = ''
        request = Request(url, callback=self.parse)
        request.meta['url'] = url
        yield request
