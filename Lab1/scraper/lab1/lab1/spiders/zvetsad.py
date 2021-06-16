import scrapy


class MebliumSpider(scrapy.Spider):
    name = "zvetsad"
    start_urls = ['https://www.zvetsad.com.ua/catalog/mnogoletnie-rasteniya-floksyi']
    XPATHS = {
        'price': '//*[contains(@class, "product__prices")]/text()',
        'description': '//*[contains(@class, "typography")]/p/span/text()',
        'image': '(//a[contains(@target, "_blank")])[1]/@href',
        'product_link': '//a[contains(@class, "product-image__body")]/@href',
    }

    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 0,
        'CLOSESPIDER_ITEMCOUNT': 20,
        'ITEM_PIPELINES': {
            'lab1.pipelines.ZvetsadPipeline': 1,
        }
    }
    allowed_domains = [
        'www.zvetsad.com.ua',
        'zvetsad.com.ua'
    ]

    def parse_product(self, response):
        price = response.xpath(self.XPATHS['price'])
        image = response.xpath(self.XPATHS['image'])
        description = response.xpath(self.XPATHS['description'])

        yield {
            'price': price.get(),
            'description': description.get(),
            'image': image.get(),
        }

    def parse(self, response):
        links = self.extract_product_links(response)
        for link in links:
            yield response.follow(link, callback=self.parse_product)

    def extract_product_links(self, response):
        result = []
        product_links = response.xpath(self.XPATHS['product_link'])
        for product_link in product_links:
            clear_product_link = product_link.extract().strip()
            if clear_product_link:
                result.append(
                    clear_product_link
                )
        return result
