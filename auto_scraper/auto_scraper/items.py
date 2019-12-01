import scrapy


class Paragraph(scrapy.Item):
    date: str = scrapy.Field()
    category: str = scrapy.Field()
    lang: str = scrapy.Field()
    site: str = scrapy.Field()
    text: str = scrapy.Field()
