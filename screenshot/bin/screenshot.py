from selenium import webdriver
from PIL import Image
from io import BytesIO
import time
import os
from bs4 import BeautifulSoup
from urllib import request

def start(driver, URL):
    driver.get(URL)
    #driver.maximize_window()
    try:
        load(driver)
        name = driver.find_element_by_class_name('sku-name').text.replace("/", " ")
        dir_path = 'C:/Users/CMA/Desktop/tb/' + name + '/'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        driver.find_element_by_class_name('ssd-module-wrap')
    except:
        source = driver.page_source
        driver.close()
        #print("无法截图,直接下载图片")

        soup = BeautifulSoup(source, 'lxml')
        images = soup.find(id="J-detail-content").find_all("img")
        for image in images:
            url = image.get('src')
            url = url.replace("https:","")
            url = "https:" + url
            print(url)
            image_guid = url.split('/')[-1]
            if len(url) != 0:
                request.urlretrieve(url, dir_path+image_guid)
    else:
        getScreenshot(driver, dir_path)

def load(driver):
    detailDiv = driver.find_element_by_id('J-detail-content')
    part = detailDiv.size['height'] // 3000
    for i in range(0, part + 1):
        js = 'window.scrollTo(0,' + str(detailDiv.location['y'] + 3000 * i) + ')'
        driver.execute_script(js)
        time.sleep(2)

def formatImage(image,path):
    width = image.width
    height = image.height
    part = height//2400

    for i in range(0,part):
        image_name = 'detail-'+str(i)+'.png'
        path = path+image_name
        image.crop((0, 2400*i, width, 2400*(i+1))).save(path)

    image_name = 'detail-'+str(part)+'.png'
    path = path + image_name
    image.crop((0, 2400*part, width, height)).save(path)

def getScreenshot(driver, path):
    detailDiv = driver.find_element_by_id('J-detail-content')
    detail = driver.find_element_by_class_name('ssd-module-wrap')

    png = driver.find_element_by_tag_name("body").screenshot_as_png

    im = Image.open(BytesIO(png))

    left = detail.location['x']
    top = detailDiv.location['y']
    right = detail.location['x'] + detail.size['width']
    bottom = detail.location['y'] + detail.size['height']


    driver.close()
    im = im.crop((left, top, right, bottom))
    if im.height < 2500:
        im.save(path)
    else:
        formatImage(im,path)



#driver = webdriver.Chrome('..//chromedriver.exe')
driver = webdriver.PhantomJS('..\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
#driver = webdriver.Firefox(options=options,executable_path=r'..\\geckodriver.exe')
start(driver, 'https://item.jd.com/100001155819.html')

#https://item.jd.com/100001155819.html 特殊情况 打算用爬虫去爬









