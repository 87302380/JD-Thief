from selenium import webdriver
from PIL import Image
from io import BytesIO
import time

# options = Options()
# options.headless = False



#driver = webdriver.Chrome('..//chromedriver.exe')
driver = webdriver.PhantomJS('..\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
#driver = webdriver.Firefox(options=options,executable_path=r'..\\geckodriver.exe')

driver.get('https://item.jd.com/100002237037.html')
driver.maximize_window()


detail = driver.find_element_by_id('J-detail-content')
location = detail.location
size = detail.size
part = detail.size['height']//2400
for i in range(0,part+1):
    js = 'window.scrollTo(0,' + str(location['y'] + 2400*i)+ ')'
    driver.execute_script(js)
    time.sleep(2)

png = driver.find_element_by_tag_name("body").screenshot_as_png

driver.close()

im = Image.open(BytesIO(png))
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

im = im.crop((left, top, right, bottom))
im.save('../screenshot.png')



