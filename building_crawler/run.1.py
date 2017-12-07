# coding = utf-8
"""
安居客爬去任务主程序
"""

from urlManager import UrlManager
from urllib.request import urlopen
from bs4 import BeautifulSoup
# from crawler import WebRequester, HTMLResolver

import re
import datetime
import pymysql.cursors

citys = ['hz', 'nj', 'bj', 'xm', 'qd', 'hn']

start = datetime.datetime.now()
for city in citys:

    urlm = UrlManager('https://' + city + '.fang.anjuke.com/loupan/all/')
    # wbrq = WebRequester()
    # slvr = HTMLResolver()

    while True:
        url = urlm.geturl()
        if url == None:
            break
        resp = urlopen(urlm.geturl())
        bsObj = BeautifulSoup(resp, 'html5lib')
        next_url = bsObj.find(resp, 'a', class_='next-page next-link')
        items = bsObj.findAll(resp, 'div', class_='item-mod', rel='nofollow')

        if next_url != None:
            urlm.addurl(next_url.attrs['href'])

        for item in items:
            try:
                name = item.find(class_='lp-name').h3.string  # 楼盘名称
                # if name:
                #     name = name.string
                # else:
                #     name = item.find('div', class_='lp-name')
                address = item.find(
                    'a', class_='address').get_text().strip()  # 楼盘地址

                huxing = item.find('a', class_='huxing')  # 楼盘户型
                if huxing != None:
                    huxing = re.sub(r'[户型：|建筑面积：|\s]', '', huxing.get_text())

                tags = ''
                for tag in item.findAll('span', class_='tag'):
                    tags += tag.get_text() + ', '
                tags.strip(', ')

                # 楼盘的价格和楼盘周边价格不同时存在
                price = item.find('p', class_='price')  # 楼盘价格
                aroundPrice = item.find(
                    'p', class_='favor-tag around-price')  # 楼盘周边价格
                if price:
                    price = price.span.string
                elif aroundPrice:
                    aroundPrice = aroundPrice.span.string

                tel = item.find('p', class_='tel')  # 咨询电话
                if tel:
                    tel = re.match(r'([\d-]+)', tel.get_text()).group()

                imgUrl = item.find(
                    'a', class_='pic').img.attrs['src']  # 效果图url
            except Exception as e:
                continue
            # test：将楼盘信息打印出来
            # print(
            #     '===============================================\n楼盘名：%s\n地址：%s\n户型：%s\n特点：%s\n价格：%s\n周边价格：%s\n电话：%s\n图像url:%s\n'
            #     % (name, address, huxing, tags, price, aroundPrice, tel, imgUrl))

            # # ---save data into a text file:--- #
            # with open('loupandata_'+city+'.txt', 'ab') as f:
            #     # string = ('===============================================\n楼盘名：%s\n地址：%s\n户型：%s\n特点：%s\n价格：%s\n周边价格：%s\n电话：%s\n图像url:%s\n'
            #     #     % (name, address, huxing, tags, price, aroundPrice, tel,
            #     #     imgUrl)).encode()
            #     string = ('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (name, address, huxing, tags, price, aroundPrice, tel, imgUrl)).encode()
            #     f.write(string)

            # ---- save data into mysql ---- #
            config = {
                'host': 'localhost',
                'user': 'root',
                'password': 'xsk123830',
                'db': 'building',
                'charset': 'utf8mb4'
            }
            sql = 'insert into property (name, address, huxing, tags, price, around_price, tel, img_url, city_id) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            conn = pymysql.connect(**config)
            try:
                with conn.cursor() as cur:
                    cur.execute(sql,
                                (name, address, huxing, tags, price, aroundPrice,
                                tel, imgUrl, str(citys.index(city) + 1)))
                    conn.commit()
            finally:
                conn.close()

        urlm.processed()
end = datetime.datetime.now()
print('共用时：%s' % str(end - start))
