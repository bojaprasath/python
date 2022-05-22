# i = 10000000000000
# print(id(i))
# j = 10
# print(id(j))
# k = i
# print(id(k))
#
#
#
# def add(a,b):
#     print(a,b)
#     print(a+b)
#     return a+b
#
# add(2,3)
# add(2,3)
#
# import os
# print(i.__sizeof__())
# str1 = 'hello'
# print(type(str1))
# l = 10,20,30
# m = 40,50,60
# print(l,type(l))
# l.__add__(m)
# print(l)
#
# print(range(100,0,-1))
#
# # a = 'asds'
# #bytearray'
# import sys
# try:
#     print(a)
#     print('Hello')
#     raise BaseException('my own ex')
# except NameError as e:
#     print(e)
#     print(sys.exc_info())
# except BaseException as e:
#     print(e)
# except:
#     pass

import re
a = '12'
m = re.search('([a])',a)
print(m)
if m:
    print(True)
else:
    print(False)

o = object()
print(o,type(o))


o = range(0,1000000)
print(o.__sizeof__())

o = xrange(0,100000)
print(o.__sizeof__())

lst1 = [i for i in range(5)]
print(lst1)


lst1 = [i*i for i in range(5)   ]
print(lst1)

###help and docstring 
###help and docstring 
###help and docstring


def fun(a):
    print('done')
print(help(fun))