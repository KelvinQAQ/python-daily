# coding = utf-8
"""
实践项目01
时间：2017-11-07
主题：强口令检测
描述：提供了一个函数，使用正则表达式，以模拟网页中的口令强度检测。强口令定义为：长度不少于8个字符，同时包含大小写字母，至少有一位数字。
"""

import re


def pwdCheck(pwd):
    # a = re.match(r'\w{8:}', pwd)
    # b = re.match(r'[A-Z]+', pwd)
    # c = re.match(r'[a-z]+', pwd)
    # d = re.match(r'[0-9]+', pwd)

    "(?=...)为预匹配，为同时满足多个条件的字符串匹配提供了方便的途径"
    if re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$', pwd):
        print('string:  "%s"  matchs!' % pwd)
    else:
        print('string:  "%s"  don\'t match!' % pwd)


pwdCheck('123')
pwdCheck('1456aB9')
pwdCheck('123w12345')
pwdCheck('a12312s12')
pwdCheck('A12312s12')
