import numpy as np
import math
import copy

# dt = np.dtype([('age', np.int8)])
# a = np.array([(10,), (20,), (30,)], dtype=dt)
# print(a['age'])

# a = np.array([[1, 2, 3], [4, 5, 6]])
# a.shape = (3, 2)
# b = a.reshape(3,2)
# print(a)
# print(b)
# print(a.flags)

# x = [[1, 2], [2, 3]]
# a = np.asarray(x, 'S4')
# print(a)

# l = range(5)
# it = iter(l)
# x = np.fromiter(it, 'f')
# print(x)

# s = 'Hello World!'
# siter = iter(s)
# a = np.fromiter(s, 'U1')
# print(a)

# a = np.linspace(0, 1, 5, dtype='f')
# print(a)

# a = np.logspace(1.0, 2.0, num = 5)
# print(a)
# b = np.linspace(1, 2, 5, dtype='f')
# print(b)

# a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# print(a[1:,2:])

# a = np.array([1,2,3,4]) 
# b = np.array([[10,20,30,40], [11, 21, 31, 41]]) 
# c = a * b 
# print(c)

# a = np.arange(0,60,5) 
# a = a.reshape(3,4)  
# print('原始数组是：')  
# print(a)
# print('修改后的数组是：')
# for x in np.nditer(a):  
#     print(x,end=' ')

# a = np.array([[1,2,3],[3,4,5],[4,5,6]])
# print('转置之前：')
# print(a)
# print('转置之后：')
# print(a.T)

# a = np.arange(0, 60, 5)
# a.shape = (3, 4)
# print(a)
# for x in np.nditer(a, flags = ['external_loop'], order = 'C'):  # 默认C风格的按行遍历
#     print(x, end=' ')
# print('\n')
# b = a.T
# print(b)
# c = a.copy(order='F')
# print(c)
# for x in np.nditer(c):  # F风格的按列遍历
#     print(x, end=' ')
# print('\n')

# a = np.arange(0,60,5)
# a.shape = (3, 4)
# print(np.transpose(a, [0, 1]))

# x = np.array([[1], [2], [3]])
# y = np.array([4, 5, 6])
# b = np.broadcast(x, y)
# r, c = b.iters
# while True:
#     try:
#         print('%2.2f, %2.2f' % (next(r), next(c)))
#     except:
#         break

# x = np.arange(36)
# print(x)
# x.shape = (3, 12)
# print(x)
# y = x.reshape((4, -1))
# print(y)

# print(np.r_[1:4, 0, 4])

# a = np.floor(10*np.random.random((2,12)))
# print(a)
# b = np.hsplit(a, (2, 3, 5, 8))
# for i in b:
#     print(i)

# a = np.arange(12)**2
# i = np.array([1,2,5,4])
# print(a[i])
# i = np.array([[3, 4], [9, 6]])
# print(a[i])

# time = np.linspace(20, 145, 5)             # time scale
# data = np.sin(np.arange(20)).reshape(5,4)  # 4 time-dependent series
# print('time: %s\n' % (time,))
# print('data: %s\n' % (data,))
# ind = data.argmax(axis=0)
# print('ind: %s\n' % (ind,))
# time_max = time[ind]
# data_max = data[ind, range(4)]
# print('time_max: %s\n' % (time_max,))
# print('data_max: %s\n' % (data_max,))

# a = np.arange(12).reshape(3, 4)
# print('a:\n%s' % (a,))
# b1 = np.array([False, True, True])
# b2 = np.array([True, False, True, False])
# print(a[b1, :])
# print(a[:, b2])
# print(a[1:3, 0:3])

