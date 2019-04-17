# -*- coding: utf-8 -*-
# © 2018 QYT Technology
# Authored by: Zhao Xingtao (zxt50330@gmail.com)
from urllib import request
from bs4 import BeautifulSoup
import re
import ssl

f = open('./c.txt', 'a+')
ssl._create_default_https_context = ssl._create_unverified_context

last = 1001
url = "/book/31556/" + str(19391824) + ".html"

def get_page(url, last):
    url = "https://www.biqiuge.com" + url
    try:
        response = request.urlopen(url, timeout=2000)
    except:
        try:
            response = request.urlopen(url, timeout=2000)
        except:
            raise
    last = last + 1

    soup = BeautifulSoup(response.read(), "html5lib")
    title = str(soup.h1)
    print(title)
    now = int(re.findall('\d+', title)[1])
    print(now)
    print(last)
    if now != last:
        raise
    f.writelines('\n')
    f.writelines(title)

    content = soup.select('.showtxt')[0]
    mystr = str(content)
    mystr = mystr.replace('\n<br/>\n<br/>\xa0\xa0\xa0\xa0\xa0\xa0\xa0\xa0', '\r\n')
    f.write(mystr)
    f.writelines('\r\n')
    next_url = soup.select('li')[-2].a['href']
    get_page(next_url, last)

if __name__ == '__main__':
    get_page(url, last)

