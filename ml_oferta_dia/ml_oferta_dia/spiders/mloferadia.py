import scrapy


class MloferadiaSpider(scrapy.Spider):
    name = "mloferadia"
    allowed_domains = ["www.mercadolivre.com.br"]
    start_urls = ["https://www.mercadolivre.com.br/ofertas"]

    def parse(self, response):
        pass
