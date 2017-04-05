import scrapy
from scrapy.selector import Selector

from ..items import ImageItem


class ImageSpider(scrapy.Spider):
    name = "image"
    xpath_image = ".//*[@id='content']/section/div/div/div/div/div/figure/a/img/@src"
    xpath_title = "//div[contains(@class, 'blog-list-item')]/div[contains(@class, 'row')]/div[contains(@class, 'col-lg-12 col-sm-12 col-xs-12')]/div[contains(@class, 'blog-item')]/header[contains(@class, 'blog-header clearfix')]/h4[contains(@class, 'blog-title')]/a/text()"

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

        elements = Selector(response=response).xpath(self.xpath_image).extract()
        titles = Selector(response=response).xpath(self.xpath_title).extract()

        for i in range(len(elements)):
            yield ImageItem(image_url=elements[i], title=titles[i])

        self.url_dict[url] = 1

