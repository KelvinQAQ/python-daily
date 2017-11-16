# coding = utf-8
"""
================================================================
这是一个爬虫程序，用来爬取安居客网页上的在售楼房信息，并存储到数据库中
项目开始时间：2017-11-08
================================================================

开发日志：
------------------------
2017-11-08
完成版本：demo

构建基本的爬虫功能，爬取对应项目的标签，但遇到了处理None类型的问题。
有些item缺少户型数据标签，导致爬虫崩溃。

------------------------
2017-11-09
完成版本 v0.1.0

更新内容：
1. 初步处理了碰到None类型的问题，但现在对None问题的处理还不完美
2. 对函数进行了封装，方便操作
3. 增加了对MySQL存储的支持

------------------------
2017-11-14



"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql.cursors
import re
import datetime


class BCrawler(object):
    startPage = 'https://nj.fang.anjuke.com/loupan/'  # 起始页
    conn = None

    # def __init__(self, startPage):
    #     self.startPage = startPage
    #     conn = None
    #     pass

    def getResponse(self, url=startPage):
        # 发送请求，并创建BeautifulSoup对象
        return urlopen(url)

    def getBsObj(self, resp):
        return BeautifulSoup(resp, 'html.parser')

    def getItems(self, bsObj):
        # 解析其中的各个楼盘信息
        return bsObj.findAll('div', class_='item-mod', rel='nofollow')

    def getData(self, item):
        # 提取每个楼盘的关键信息
        name = item.find('span', class_='items-name').string  # 楼盘名称
        address = item.find('a', class_='address').get_text().strip()  # 楼盘地址

        huxing = item.find('a', class_='huxing')  # 楼盘户型
        if huxing != None:
            huxing = re.sub(r'[户型：|建筑面积：|\s]', '', huxing.get_text())

        tags = re.sub(r'\S\n', ' ',
                      item.find('div', class_='tag-panel').get_text())  # 楼盘特征

        # 楼盘的价格和楼盘周边价格不同时存在
        price = item.find('p', class_='price')  # 楼盘价格
        aroundPrice = item.find('p', class_='favor-tag around-price')  # 楼盘周边价格
        if price:
            price = price.span.string
        else:
            aroundPrice = aroundPrice.span.string

        tel = item.find('p', class_='tel')  # 咨询电话
        if tel:
            tel = re.match(r'([\d-]+)', tel.get_text()).group()

        imgUrl = item.find('a', class_='pic').img.attrs['src']  # 效果图url

        return {
            'name': name,
            'address': address,
            'huxing': huxing,
            'tags': tags,
            'price': price,
            'aroundPrice': aroundPrice,
            'tel': tel,
            'imgUrl': imgUrl
        }

    def connect(self, *args, **kwargs):
        self.conn = pymysql.connect(*args, **kwargs)

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def save2MySQL(self, data):
        with self.conn.cursor() as cur:
            sql = 'insert into Building (name, address, huxing, tags, price, aroundPrice, tel, imgUrl) values (%s, %s, %s, %s, %s, %s, %s, %s)'
            count = cur.execute(
                sql, (data['name'], data['address'], data['huxing'],
                      data['tags'], data['price'], data['aroundPrice'],
                      data['tel'], data['imgUrl']))
            if count:
                self.conn.commit()

    def run(self):
        resp = self.getResponse()
        bsObj = self.getBsObj(resp)
        items = self.getItems(bsObj)

        self.connect(
            host='localhost',
            user='root',
            password='xsk123830',
            db='url_database',
            charset='utf8mb4')

        try:
            for item in items:
                data = self.getData(item)
                self.save2MySQL(data)
        finally:
            self.disconnect()

    def test(self):
        resp = self.getResponse()
        bsObj = self.getBsObj(resp)
        items = self.getItems(bsObj)

        self.connect(
            host='localhost',
            user='root',
            password='xsk123830',
            db='url_database',
            charset='utf8mb4')

        try:
            for item in items:
                data = self.getData(item)
                self.save2MySQL(data)
        finally:
            self.disconnect()




if __name__ == '__main__':
    bCrawler = BCrawler()
    bCrawler.test()

# # 起始页面为安居客南京楼盘页面
# startPage = 'https://nj.fang.anjuke.com/loupan/'

# # 发送请求，并创建BeautifulSoup对象
# resp = urlopen(startPage)
# bsObj = BeautifulSoup(resp, 'html.parser')

# # 解析其中的各个楼盘信息
# items = bsObj.findAll(
#     'div', class_='item-mod', rel='nofollow')  # item-mod包含一个楼盘的所有信息，先将其全部提取出来

# for item in items:
#     # 提取每个楼盘的关键信息
#     name = item.find('span', class_='items-name').string  # 楼盘名称
#     address = item.find('a', class_='address').get_text().strip()  # 楼盘地址

#     huxing = item.find('a', class_='huxing')  # 楼盘户型
#     if huxing != None:
#         huxing = re.sub(r'[户型：|建筑面积：|\s]', '', huxing.get_text())

#     tags = re.sub(r'\S\n', ' ',
#                   item.find('div', class_='tag-panel').get_text())  # 楼盘特征

#     # 楼盘的价格和楼盘周边价格不同时存在
#     price = item.find('p', class_='price')  # 楼盘价格
#     aroundPrice = item.find('p', class_='favor-tag around-price')  # 楼盘周边价格
#     if price:
#         price = price.span.string
#     else:
#         aroundPrice = aroundPrice.span.string

#     tel = item.find('p', class_='tel')  # 咨询电话
#     if tel:
#         tel = re.match(r'([\d-]+)', tel.get_text()).group()

#     imgUrl = item.find('a', class_='pic').img.attrs['src']  # 效果图url

#     # # test：将楼盘信息打印出来
#     # print(
#     #     '===============================================\n楼盘名：%s\n地址：%s\n户型：%s\n特点：%s\n价格：%s\n周边价格：%s\n电话：%s\n图像url:%s\n'
#     #     % (name, address, huxing, tags, price, aroundPrice, tel, imgUrl))
