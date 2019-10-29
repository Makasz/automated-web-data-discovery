import scrapy


class Advertisement(scrapy.Item):
    """One single advertisement from a website"""
    date: str = scrapy.Field()
    country: str = scrapy.Field()
    platform: str = scrapy.Field()
    fact_type: str = scrapy.Field()
    r1: str = scrapy.Field()
