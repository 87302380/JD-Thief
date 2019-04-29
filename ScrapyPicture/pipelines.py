# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os

class ScrapypicturePipeline(ImagesPipeline):
    #def process_item(self, item, spider):
    #    return item
    # 获取settings文件里设置的变量值
    #IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):

        image_url = item["pic_path"][:]

        yield scrapy.Request(image_url, meta={'item':item,'index':item['pic_path'].index(image_url)})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']  # 通过meta把item值传递过来

        image_guid =  request.url.split('/')[-1]

        filename = item['src_contents'].replace("/"," ") + "/" + image_guid
        print(filename)
        return filename


