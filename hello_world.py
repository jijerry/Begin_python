#!/usr/bin/env python3


# a, b = 0, 1
# while b < 100:
#     print(b, end=' ')
#     a, b = b, a + b
#
#
# def sum(a, b):
#     return a + b
#
#
# res = sum(123123, 14314)
# print(res)


# 复制文件
# import sys
#
# if len(sys.argv) < 3:
#     print("wrong parameter")
#     print("./copyfile.py files file2")
#     sys.exit(1)
#
# f1 = open(sys.argv[1])
# s = f1.read()
# f1.close()
#
# f2 = open(sys.argv[2], 'w')
# f2.write(s)
# f2.close()


# 类的继承
# class Person(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def get_details(self):
#         return self.name
#
# class Student(Person):
#
#     def __init__(self, name, branch, year):
#         Person.__init__(self, name)
#         self.branch = branch
#         self.year = year
#
#     def get_details(self):
#
#         return "{} student {} and is in {} year".format(self.name, self.branch, self.year)
#
# class Teacher(Person):
#
#     def __init__(self, name, papers):
#         Person.__init__(self, name)
#         self.papaers = papers
#
#     def get_details(self):
#         return  "{} teachers {}".format(self.name, ','.join(self.papaers))
#
#
# person1 = Person('jerry')
# student1 = Student('jerry1', 'sce', 2005)
# teacher1 = Teacher('jerr2', ['c', 'c++'])
#
# print(person1.get_details())
# print(student1.get_details())
# print(teacher1.get_details())



# 装饰器
# class Account(object):
#
#     def __init__(self, rate):
#         self.__amt = 0
#         self.rate = rate
#
#     @property
#     def amount(self):
#         print('hello')
#         return self.__amt
#
#     @property
#     def cny(self):
#         return  self.__amt * self.rate
#
#     @amount.setter
#
#     def amount(self, value):
#         if value < 0:
#             print("sorry, no negative amount in the account")
#             return
#         self.__amt = value
#
#
# if __name__ == '__main__':
#
#     acc = Account(rate=6.6)
#     acc.amount = 20
#
#     print("dollar:", acc.amount)
#     print("cny:", acc.cny)
#
#     acc.amount = -100
#     print("amount:", acc.amount)

