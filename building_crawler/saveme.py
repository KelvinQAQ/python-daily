# coding = utf-8
"""
这是一个负责存储数据的模块
能够将数据存储到文件
也能够将数据存储到MySQL数据库中
"""

import pymysql
import pymysql.connections


class Connection(object):
    def __init__(self, connstr):
        self.connstr = connstr
        pass

    @property
    def connstr(self):
        return self.__connstr

    @connstr.setter
    def connstr(self, connstr):
        self.__connstr = connstr

    @property
    def conn(self):
        return self.__conn

    def open(self):
        try:
            self.__conn = pymysql.connect(**self.connstr)
        except Exception as e:
            print('<Error!>: %s' % (e.__context__, ))

    def execute(self, sqlstr, args=None):
        with self.conn.cursor() as cur:
            count = cur.execute(sqlstr, args=None)
            if count:
                self.conn.commit()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

