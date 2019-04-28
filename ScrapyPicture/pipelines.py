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
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):

        image_url = item["pic_path"][:]

        yield scrapy.Request(image_url)

        '''
        for p in range(2,51):
            image_url = item["pic_path"][:-5]+str(p)+'.jpg'
            print(image_url)
            #image_referer = item["pic_url"][:-5]+'_'+str(p)+'.html'

            #print(image_referer)
            
        '''


