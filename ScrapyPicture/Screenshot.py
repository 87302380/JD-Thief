from selenium import webdriver
from PIL import Image
from io import BytesIO
import time
import os

class Screenshot(object):

    url = ""

    def __init__(self, url):
        self.url = url

    def formatImage(self,image,name):
        width = image.width
        height = image.height
        part = height//2400
        dir_path = 'C:/Users/CMA/Desktop/tb/' + name + '/'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for i in range(0,part):
            image_name = 'detail-'+str(i)+'.png'
            path = dir_path+image_name
            image.crop((0, 2400*i, width, 2400*(i+1))).save(path)

        image_name = 'detail-'+str(part)+'.png'
        path = dir_path + image_name
        image.crop((0, 2400*part, width, height)).save(path)

    def getScreenshot(self,driver):
        detailDiv = driver.find_element_by_id('J-detail-content')
        detail = driver.find_element_by_class_name('ssd-module-wrap')
        part = detail.size['height'] // 3000
        for i in range(0, part + 1):
            js = 'window.scrollTo(0,' + str(detail.location['y'] + 3000 * i) + ')'
            driver.execute_script(js)
            time.sleep(2)

        png = driver.find_element_by_tag_name("body").screenshot_as_png

        im = Image.open(BytesIO(png))

        left = detail.location['x']
        top = detailDiv.location['y']
        right = detail.location['x'] + detail.size['width']
        bottom = detail.location['y'] + detail.size['height']

        name = driver.find_element_by_class_name('sku-name').text.replace("/", " ")

        driver.close()
        im = im.crop((left, top, right, bottom))
        if im.height < 2500:
            dir_path = 'C:/Users/CMA/Desktop/tb/' + name + '/'
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            im.save('C:/Users/CMA/Desktop/tb/' + name + '/detail.png')
        else:
            self.formatImage(im,name)

    def start(self,url):
        driver = webdriver.PhantomJS('../ScrapyPicture/phantomjs-2.1.1-windows/bin/phantomjs.exe')
        driver.get(url)
        #driver.maximize_window()
        try:
            driver.find_element_by_class_name('ssd-module-wrap')
        except:
            print("无法截图,使用爬虫获取详情")
            driver.close()
        else:
            self.getScreenshot(driver)














