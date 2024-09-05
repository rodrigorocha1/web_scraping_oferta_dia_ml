import scrapy
from scrapy.http import Response
from itertools import zip_longest
from scrapy.selector import Selector


class MloferadiaSpider(scrapy.Spider):
    name = "mloferadia"
    allowed_domains = ["www.mercadolivre.com.br"]
    start_urls = ["https://www.mercadolivre.com.br/ofertas"]
    pagina_inicio = 1
    pagina_fim = 3

    def parse(self, response: Response):
        nome_produtos = response.xpath(
            '//p[@class="promotion-item__title"]/text()').getall()
        precos = response.xpath(
            '//span[@class="andes-money-amount andes-money-amount--cents-superscript"]').getall()
        imagens_produtos = response.css(
            'img.promotion-item__img::attr(src)').getall()
        marcas = response.css('li.promotion-item')
        url_para_pegar_o_id = response.css(
            'a.promotion-item__link-container::attr(href)').getall()

        for nome_produto, preco, imagem, marca, url_id in zip_longest(nome_produtos, precos, imagens_produtos, marcas, url_para_pegar_o_id):
            preco_reais = Selector(text=preco).xpath(
                '//span[@class="andes-money-amount__fraction"]/text()').get()
            preco_centavos = Selector(text=preco).xpath(
                '//span[@class="andes-money-amount__cents andes-money-amount__cents--superscript-24"]/text()').get()
            yield {
                'nome_produto': nome_produto,
                'preco_reais': preco_reais,
                'preco_centavos': preco_centavos,
                'imagem': imagem,
                'marcas': marca.css('span.promotion-item__seller::text').get(),
                'url_id': url_id

            }
