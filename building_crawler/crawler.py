# coding: utf-8

"""
这是一个网页请求模块
功能是向urlManager请求一个url然后尝试获取response
然后向urlManager反馈，并向HTML解析器传输
"""

from urllib.request import urlopen
from urlManager import UrlManager
from bs4 import BeautifulSoup
import re


class WebRequester(object):

    def __init__(self):
        pass

    @staticmethod
    def request(urlManager):
        url = urlManager.geturl()
        resp = urlopen(url)
        urlManager.processed()
        return resp

class HTMLResolver(object):
    
    def __init__(self):
        pass

    @staticmethod
    def getItems(resp, tags, attrs={}, **kwargs):
        bsObj = BeautifulSoup(resp, 'html5lib')
        items = bsObj.findAll(name=tags, attrs=attrs, **kwargs)
        return items

    @staticmethod
    def getItem(resp, tag, attrs={}, **kwargs):
        bsObj = BeautifulSoup(resp, 'html5lib')
        item = bsObj.find(name=tag, attrs=attrs, **kwargs)
        return item

if __name__ == '__main__':
    urlManager = UrlManager('http://en.wikipedia.org/wiki/Main_Page')
    for i in range(1, 101):
        print('crawling No.%d url...' % (i,))
        resp = WebRequester.request(urlManager)
        items = HTMLResolver.getItems(resp, 'a', href=re.compile(r'(?!.+\.\w+$)(^/wiki)'))
        for item in items:
            fullurl = 'http://en.wikipedia.org' + item.attrs['href']
            b = urlManager.addurl(fullurl)
            if b:
                with open('urls.txt', 'a') as f:
                    f.write(fullurl + '\n')
    # with open('urls.txt', 'ab') as f:
    #     f.writelines(urlManager.new_urls)
    #     f.writelines(urlManager.done_urls)
                