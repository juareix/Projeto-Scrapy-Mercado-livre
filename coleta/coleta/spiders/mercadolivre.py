import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-de-corrida-masculino"]

    def parse(self, response):
        products = response.css('div.ui-search-result__content') # 54 itens

        for product in products:

            prices = product.css('span.andes-money-amount__fraction::text').getall()

            yield {
                'brand': product.css('span.ui-search-item__brand-discoverability.ui-search-item__group__element::text').get(),
            }