import scrapy
from ScrapyPicture import items


class Thief(scrapy.Spider):
    name = 'thief'

    url = "https://item.jd.com/5564722.html"
    start_urls = [url]

    def parse(self, response):

        base_pic_list = response.xpath("//ul[@class='lh']/li/img/@src")
        deatil_path = response.xpath("//div[@id = 'J-detail-content']//img/@data-lazyload")
        name = response.xpath("//div[@class='sku-name']/text()")

        name = name.extract()[len(name)-1].strip()

        item = items.ScrapypictureItem()

        item['src_contents'] = name

        for each in deatil_path:
            pic_path = str(each.extract()).replace("https:","")
            pic_path = "https:" + pic_path
            item["pic_path"] = pic_path
            yield item

        for each in base_pic_list:

            path = "https:" + each.extract()

            if path.find('com/n5'):
                path = path.replace('com/n5', 'com/n1')
            else:
                path = path.replace('com/n1', 'com/n5')
            path = path.replace('s54x54', 's450x450')
            item["pic_path"] = path
            yield item






