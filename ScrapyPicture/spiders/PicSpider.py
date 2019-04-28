import scrapy
from ScrapyPicture import items
import datetime


class PicSpider(scrapy.Spider):
    name = 'porter'

    url = "https://item.jd.com/502250.html"

    start_urls = [url]

    def parse(self, response):

        base_pic_list = response.xpath("//ul[@class='lh']/li/img/@src")

        for each in base_pic_list:
            item = items.ScrapypictureItem()
            path = "https:" + each.extract()

            if path.find('com/n5'):
                path = path.replace('com/n5', 'com/n1')
            else:
                path = path.replace('com/n1', 'com/n5')
            path = path.replace('s54x54', 's450x450')
            item["pic_path"] = path
            #item["pic_url"] = each.xpath('./a/@href').extract()[0]
            yield item

