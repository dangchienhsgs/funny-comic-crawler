import scrapy
from scrapy.selector import Selector
from ..items import ImageItem


class ImageSpider(scrapy.Spider):
    name = "image"
    xpath = ".//*[@id='content']/section/div/div/div/div/div/figure/a/img/@src"

    url_dict = {}

    def start_requests(self):
        i = 1

        while True:
            url = 'http://kimchicucai.com/kim-chi-cu-cai-1/?q=&page={}'.format(i)
            i += 1
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        url = response.url
        if url in self.url_dict.keys():
            return

        elements = Selector(response=response).xpath(self.xpath).extract()
        for element in elements:
            yield ImageItem(image_urls=[element])

        self.url_dict[url] = 1