import numpy as np
import matplotlib.pyplot as plt
import time


def actv_func(x):
    """
    Activating function
    If x is negetive, return -1, otherwise return 1
    imput: x
    output: sgn(x)
    """
    if x >=0:
        return 1
    else:
        return -1

class Perceptron(object):

    __size__ = None
    __weight__ = None
    __acfun__ = None

    def __init__(self, size, acfun=actv_func):
        self.__size__ = size
        self.__weight__ = 2*np.random.random(self.__size__+1) - 1
        self.__acfun__ = acfun
        pass

    def train(self, datas, expects, eta=0.01, epoch=100):
        for i in range(epoch):
            count = 0       # 每轮训练中错误的次数
            for index in range(datas.shape[0]):
                y = self.__acfun__(np.dot(datas[index], self.__weight__))
                if y*expects[index] < 0:
                    count += 1
                    self.__weight__ += (eta*datas[index]*expects[index])
                    # print((eta*datas[index]*expects[index]))
            print('Now epoch: %s' % (i+1,))
            print('Weight: %s' % (self.__weight__))
            print('Error counts: %s' % (count,))
            print('Error rate: %s' % (count/datas.shape[0],))
            print('--------------------')
            time.sleep(0.1)
            if count == 0:
                break


if __name__ == '__main__':
    datas = np.hstack([np.ones([100, 1]), np.vstack([np.random.rand(50, 5), -1*np.random.rand(50, 5)])])
    expects = np.hstack([-1*np.ones(50, dtype='i'), np.ones(50, dtype='i')])
    plt.plot(datas, expects)
    pre = Perceptron(5)
    pre.train(datas, expects)

    # print(datas[0])
    # print(datas.shape)
    # print(expects.shape)