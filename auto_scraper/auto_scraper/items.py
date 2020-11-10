import scrapy


class Paragraph(scrapy.Item):
    date: str = scrapy.Field()
    category: str = scrapy.Field()
    lang: str = scrapy.Field()
    site: str = scrapy.Field()
    _text: str = scrapy.Field()
    _name_index: str = scrapy.Field()
    source_url: str = scrapy.Field()

