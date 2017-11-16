# coding: utf-8

"""
这是一个网页请求模块
功能是向urlManager请求一个url然后尝试获取response
然后向urlManager反馈，并向HTML解析器传输
"""

from urllib.request import urlopen
from urlManager import UrlManager


class WebRequester(object):

    url = ''

    def __init__(self):
        pass

