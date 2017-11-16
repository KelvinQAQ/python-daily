# coding = utf-8
"""
实践项目2：
时间：2017-11-08
主题：自定义strip()函数
描述：实现strip()函数的相应功能，并使用第二个可选参数去除对应的字符。
"""

import re


def my_strip(string, pattern=None):
    # 若第二个可选参数值为None，实现strip()函数的相应功能
    if not pattern:
        return string.strip()
    else:
        # re.sub()的用法要牢记！
        return re.sub(pattern, '', string=string)


if __name__ == '__main__':
    print(my_strip('  /asdf  '))
    print(my_strip('abcabcabcdcdcdcabcabc', 'dc'))