# coding = utf-8

"""
这是building_crawler项目中的URL管理模块
主要实现的功能是存储URL、给网页请求器发送待爬URL、接受新的URL
这是多进程的版本

======== 开发日志 ========
2017.12.04
内容：框架编写
"""

class UrlManagerMP(object):
    
    new_urls = []       # 未爬url
    buff = {}           # 暂存被请求的url
    done_urls = []      # 已爬url或失效url
    # processing = False  # 指示是否有url正在被请求
    
    def __init__(self, start_urls):     # 初始化，存入起始url地址
        for url in start_urls:
            self.new_urls.append(url)
        pass
    
    def geturl(self):
        if len(self.new_urls) != 0:
            self.processing = True
            return self.new_urls[0]  # 返回new_urls的第一个
        else:
            return None              # 如果new_urls为空数组，返回None
    
    def addurl(self, url):
        if (url not in self.done_urls) and (url not in self.new_urls):
            print('add a new url...  <%s>' % (url,))
            self.new_urls.append(url)
            return True
        else:
            return False

    def processed(self):
        if self.processing:
            print('a url has been processed...  <%s>' % (self.new_urls[0],))
            self.done_urls.append(self.new_urls[0])
            del self.new_urls[0]
            self.processing = False
        else:
            print('<Error> There is no url processing...')

    @property
    def count(self):
        return [len(self.new_urls), len(self.done_urls)]

# if __name__ == '__main__':
#     urlManager = UrlManager('http://www.baidu.com')
#     urlManager.addurl('http://www.qq.com')
#     urlManager.addurl('http://www.163.com')
#     urlManager.addurl('http://www.google.com')
#     urlManager.addurl('http://www.bing.com')
#     for _ in range(0, 6):
#         print('---newurls: %d,  doneurls: %d---' % tuple(urlManager.count))
#         urlManager.geturl()
#         urlManager.processed()
#         print('--------------------------------\n')
        