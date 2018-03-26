# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

index = 0
download_folder = 'images'
headers = {'referer': 'http://jandan.net/',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
driver = webdriver.PhantomJS()


#  保存图片
def save_img(res_url):
    global index

    driver.get(res_url)
    driver.save_screenshot(download_folder + '/screen-' + str(i) + '.png')

    content = driver.page_source
    html = BeautifulSoup(content, "html.parser")
    for link in html.find_all('a', {'class': 'view_img_link'}):
        with open(download_folder +
                  '/{}.{}'.format(index, link.get('href')[len(link.get('href'))-3: len(link.get('href'))]),
                  'wb') as img:
            img.write(requests.get("http:" + link.get('href')).content)
        print("正在抓取第%s条数据" % index)
        index += 1


#  抓取图片
if __name__ == '__main__':
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    url = 'http://jandan.net/ooxx'
    for i in range(0, 3):
        save_img(url)
        url = "http:" + BeautifulSoup(requests.get(url, headers=headers).text, "html.parser").\
            find('a', {'class': 'previous-comment-page'}).get('href')

    print('done')
