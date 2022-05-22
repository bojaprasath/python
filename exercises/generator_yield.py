# mygenerator = (x*x for x in range(3))
# for i in mygenerator:
#     print(i)
#
#
# def createGenerator():
#     mylist = range(3)
#     for i in mylist:
#         yield i*i
#
# mygenerator1 = createGenerator()
# for i in mygenerator1:
#     print(i)
#
# mygenerator2 = createGenerator()
# print(next(mygenerator2))
# print(next(mygenerator2))
# print(next(mygenerator2))
# # print(next(mygenerator2))

a = '12321'
b = '12'
sum = 0
def sum_string(a,b):
    i = 0
    sum = 0
    carry = 0
    for j,k in zip(a,b):
        print(j,k)
sum_string('11','21')



class C:
    def done(self):
        print('doneC')

class B:
    def done(self):
        print('doneB')

class A(B,C):
    def done1(self):
        print('done')
a = A()
b = a
c = a
a.done()
del a
b.done()


# class Robot:
#     def action(self):
#         print('Robot action')
#
# class HelloRobot(Robot):
#     def action(self):
#         print('Hello world')
#
# r = HelloRobot()
# r.action()
#
#
# class Robot:
#     def action(self):
#         print('Robot action')
#
# class HelloRobot(Robot):
#     def action(self):
#         print('Hello world')
#
# class DummyRobot(Robot):
#     def start(self):
#         print('Started.')
#
# r = HelloRobot()
# d = DummyRobot()
#
# r.action()
# d.action()
#
#
#
# a = [12,3,4]
# b = a
# c = a
# del a
# print(b)
# print(c)
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)

print(list_)
print(generator)

#https://www.askpython.com/python/python-yield-examples
#Read large file using generator

# import resource
# import sys
#
#
# def read_file(file_name):
#     text_file = open(file_name, 'r')
#     line_list = text_file.readlines()
#     text_file.close()
#     return line_list
#
#
# file_lines = read_file('iterator.txt')
#
# print(type(file_lines))
#
# print(len(file_lines))
#
# for line in file_lines:
#     print(line)
#
# print('Peak Memory Usage =', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
# print('User Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
# print('System Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_stime)

import resource
import sys


def read_file_yield(file_name):
    text_file = open(file_name, 'r')
    i = 0
    while True:
        line_data = text_file.readline()
        if not line_data:
            text_file.close()
            print(i)
            break
        i = i + 1
        print(i)
        yield line_data


file_data = read_file_yield('iterator.txt')
print(type(file_data))
import pdb;pdb.set_trace()
for l in file_data:
    print(l)

print('Peak Memory Usage =', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
print('User Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
print('System Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_stime)