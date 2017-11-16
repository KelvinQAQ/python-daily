# coding = utf-8

"""
这是building_crawler项目中的URL管理模块
主要实现的功能是存储URL、给网页请求器发送待爬URL、接受新的URL
"""

class UrlManager(object):
    
    new_urls = []    # 未爬url
    # buff = []        # 暂存被请求的url
    done_urls = []   # 已爬url或失效url
    
    def __init__(self, start_url):
        self.new_urls.append(start_url)
        pass
    
    def getMessage(self, msg):
        """
        这是UrlManager的消息管理函数，通过接收到的消息来进行不同的操作
        """
        if msg['id'] == 11:          # 如果接受到的消息是请求一个未爬的url
            # 如果未爬url非空
            if len(self.new_urls) != 0:
                return {'id':21, 'str':self.new_urls[0]}  # 返回new_urls的第一个
            else:
                return {'id':20}     # 如果new_urls尾空数组，返回None
        elif msg['id'] == 12:        # 如果接受到的消息是传递给请求器的url处理完毕
            rmsg = {'id':22, 'str':'url %s was done...' % self.new_urls[0]}
            self.done_urls.append(self.new_urls[0])
            del self.new_urls[0]
            return rmsg
        elif msg['id'] == 13:        # 如果是接受到了新的url
            if msg['id'] not in self.done_urls:
                self.new_urls.append(msg['str'])
        else:
            pass
    
    def geturl(self):
        url = self.getMessage({'id':11})['str']
        print('get a url from UrlManager...  <%s>' % (url,))
        return url
    
    def addurl(self, url):
        print('add a new url...  <%s>' % (url,))
        self.getMessage({'id':13, 'str':url})