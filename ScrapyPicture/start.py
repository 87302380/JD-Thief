# -*- coding: utf-8 -*-

from scrapy import cmdline
from ScrapyPicture.Screenshot import Screenshot
import re

def set_url(url):
    data = ""
    code = open('../ScrapyPicture/spiders/Thief.py', 'r+')
    for line in code.readlines():
        if (re.search('url = ', line)):
            line = "    url = " + "\"" + url + "\"" +"\n"
        data += line

    code = open('../ScrapyPicture/spiders/Thief.py', 'r+')
    code.writelines(data)



url = "https://item.jd.com/5564722.html"

# set_url(url)
#
# cmdline.execute("scrapy crawl thief".split())

screenshot = Screenshot(url)

screenshot.start(url)