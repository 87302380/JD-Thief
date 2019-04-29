from selenium import webdriver
from PIL import Image
from io import BytesIO
import time

#driver = webdriver.Chrome('..//chromedriver.exe')
driver = webdriver.PhantomJS('..\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
#driver = webdriver.Firefox(options=options,executable_path=r'..\\geckodriver.exe')

driver.get('https://item.jd.com/100002237037.html')
#https://item.jd.com/100001155819.html 特殊情况 打算用爬虫去爬
driver.maximize_window()

detailDiv = driver.find_element_by_id('J-detail-content')
detail = driver.find_element_by_class_name('ssd-module-wrap')

size = detail.size
part = detail.size['height']//3000
for i in range(0,part+1):
    js = 'window.scrollTo(0,' + str(detail.location['y'] + 3000*i)+ ')'
    driver.execute_script(js)
    time.sleep(2)

png = driver.find_element_by_tag_name("body").screenshot_as_png

im = Image.open(BytesIO(png))

left = detail.location['x']
top = detailDiv.location['y']
right = detail.location['x'] + detail.size['width']
bottom = detail.location['y'] + detail.size['height']

driver.close()
im = im.crop((left, top, right, bottom))

def formatImage(image):
    width = image.width
    height = image.height
    part = height//2400
    for i in range(0,part):
        path = '../image/screenshot-'+str(i)+'.png'
        image.crop((0, 2400*i, width, 2400*(i+1))).save(path)

    path = '../image/screenshot-' + str(part) + '.png'
    image.crop((0, 2400*part, width, height)).save(path)

if im.height < 2400:
    im.save('../screenshot.png')
else:
    formatImage(im)




