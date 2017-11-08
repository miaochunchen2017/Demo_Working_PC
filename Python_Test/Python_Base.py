# coding=utf-8
# 打印&赋值
import os
import time

import datetime

import sys
import types
from copy import deepcopy
from Python_Def import laugh  # 直接引入Python_Def 模块中的laugh()方法，不用再通过Python_Def创建laugh()方法的对象

# 亦可以直接引用Python_Def 模块中的所有方法，from Python_Def import *

import Python_Def  # 引用模块 Python_Def

print "\n打印&赋值："
# 打印
print 'Hello World!'
# 赋值
a = 10
print a, type(a)
a = 1.3
print a, type(a)

# 序列
print "\n序列："
# 类型为tuple，无法更改
s1 = (2, 1.3, 'love', 5.6, 9, 12, False)
# 类型为list，可以更改
s2 = [True, 5, 'smile']
print s1, type(s1)
print s2, type(s2)
s2[1] = 4
print s2, type(s2)
s3 = [1, [3, 4, 5]]
print s3[1][2]
print "数组原貌:", s1
# 从开始到下标4
print "从开始到下标4:", s1[:4]
# 从开始到结束，每隔2个元素显示
print "从开始到结束，每隔2个元素显示:", s1[::2]
# 从开始到结束，倒序打印
print "从开始到结束，倒序打印:", s1[::-1]
# 序列最后一个元素
print "最后一个元素:", s1[-1]
# 序列倒数第三个元素
print "倒数第三个元素:", s1[-3]

# 字符串
print "\n字符串："
str_1 = 'Mcc is a SUPERMAN.'
print "字符串str为:", str_1
# 显示第4位需要“str[3：”，而显示第8位则可以“str[3:8]”
print "字符串str中的第4位到第8位字符为:", str_1[3:8]

# 基础运算
print "\n基础运算："
print "1 + 9 =", 1 + 9
print "1.3 - 4 =", 1.3 - 4
print "3 * 5 =", 3 * 5
print "4.5 / 1.5 =", 4.5 / 1.5
print "3 ** 2 =", 3 ** 2
print "10 % 5 =", 10 % 5

# 判断
print "\n判断："
print "5 = 6 ?   ==>  ", 5 == 6
print "8 != 8 ?   ==>  ", 8 != 8
print "3 < 3 ?   ==>  ", 3 < 3
print "3 <= 3 ?   ==>  ", 3 <= 3
print "5 in [1,3,5] ?   ==>  ", 5 in [1, 3, 5]
print '"Mcc" is "Mcc" ?   ==>  ', "Mcc" is "Mcc"
print '"Mcc" is not "ZMR" ?   ==>  ', "Mcc" is not "ZMR"

# 逻辑运算，True/False之间的运算
print "\n逻辑运算："
# and , “与”运算，两者都为真才是真
print "True and True   ==>  ", True and True
print "True and False   ==>  ", True and False
# or , “或”运算，其中之一为真即为真
print "True or False   ==>  ", True or False
print "True or False or False   ==>  ", True or False or False
# not , “非”运算，取反
print "not True   ==>  ", not True
# 结合起来，比如：
print "5 = 6 or 3 >= 3 'True or False ?'  ==>  ", 5 == 6 or 3 >= 3

# if 条件语句
print "\nif条件语句："
print "\n例一："
i = 5
x = 1
if i > 0:
    x = x + 1
print "Q:i = 5 x = 1 if i > 0: x = x + 1 \n  x = ?", "\nA:", x

print "\n例二："
i = 1
if i > 0:
    print 'positive i'
    i = i + 1
elif i == 0:
    print 'i is 0'
    i = i * 10
else:
    print 'negative i'
    i = i - 1

print 'new i:', i

print "\n例三："
i = 5
if i > 1:
    print 'i bigger than 1'
    print 'good'
    if i > 2:
        print 'i bigger than 2'
        print 'even better'

# for 循环
print "\n for 循环："
print "\n例一："
for a in [3, 4, 5, 'life']:
    print a

print "\n例二："
# range(n)的功能是新建一个表。这个表的元素都是整数，从0开始，下一个元素比前一个大1， 直到函数中所写的上限 （不包括该上限本身）
idx = range(5)
print idx

print "\n例三："
for a in range(5):
    print a ** 2

# while 循环
print "\nwhile循环："
print "\n例一："
i = 0
while i < 10:
    print i
    i += 1

print "\n例二："
# continue 命令在循环的某一次执行中，如果遇到continue，那么跳过这一次执行，进行下一次的循环
for i in range(5):
    if i == 2:
        continue
    print i

print "\n例三："
# break 停止执行整个循环
for i in range(5):
    if i == 2:
        break
    print i

# 函数
print "\n函数："
print "\n例一："


# 定义函数，求a和b的平方和
def square_sum(a, b):
    c = a ** 2 + b ** 2
    return c


# 调用函数square_sum（a,b）
print square_sum(1, 2)

print "\n例二："
a = 1


def change_integer(a):
    a += 1
    return a


print change_integer(a)
print a

b = [1, 2, 3]


def change_list(b):
    b[0] = b[0] + 1
    return b


print change_list(b)
print b
print "第一个例子，我们将一个整数变量传递给函数，函数对它进行操作，但原整数变量a不发生变化。\n第二个例子，我们将一个列表传递给函数，函数进行操作，原来的列表 b 发生变化。\n对于基本数据类型的变量，变量传递给函数后，函数会在内存中复制一个新的变量，从而不影响原来的变量。（我们称此为值传递）\n但是对于列表来说，表传递给函数的是一个指针，指针指向序列在内存中的位置，在函数中对列表的操作将在原有内存中进行，从而影响原有变量。 （我们称此为指针传递，python 中也称为 引用传递），指针是C/C++语言中的重要概念，有关指针的概念可以到网上搜索相关资料。"

# 面向对象
print "\n面向对象："
print "\n例一：定义鸟"


class Bird(object):
    have_feather = True  # 是否有羽毛
    way_of_reproduction = 'egg'  # 生殖方式

    def move(self, dx, dy):  # 定义鸟的移动方法
        position = [0, 0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position


# 定义一个小鸡，名叫summer
summer = Bird()
print 'after move , summer at:', summer.move(5, 8)

# 面向对象：子类
print "\n面向对象：子类："
print "\n例一：定义鸡：继承鸟的部分属性"


class Chicken(Bird):  # 定义鸡类，继承了鸟类的是否有羽毛、生殖方式属性，自身增加了行动方式、是否出现在KFC属性
    way_of_move = 'walk'
    possible_in_KFC = True


class Oriole(Bird):  # 定义黄鹂类，继承了鸟类的是否有羽毛、生殖方式属性，自身增加了行动方式、是否出现在KFC属性
    way_of_move = 'fly'
    possible_in_KFC = False


summer = Chicken()
print summer.have_feather
print summer.move(5, 8)
print summer.way_of_move
print summer.possible_in_KFC

# 调用类的其他信息
print "\n通过self，调用类属性："
print "\n例一："

i = 0


class Human(object):
    laugh = 'HAHAHAHA'

    def show_laugh(self):
        print self.laugh

    def laugh_5th(self):
        for i in range(5):
            self.show_laugh()


li_lei = Human()
li_lei.laugh_5th()

print "\n__init__()方法，函数初始化："
print "\n例一："


class happyBird(Bird):
    def __init__(self, more_words):
        print 'We are happy birds.', more_words


# __init__方法必须将happyBird当做第一个实例运行
summer = happyBird('HAPPY!')

# 对象的性质，类属性之外的对象特色的性质
print "\n对象的性质："
print "\n例一："


class Human(object):
    def __init__(self, input_gender, input_color):
        # 将参数input_gender 赋值给对象的性质，即self.gender
        self.gender = input_gender
        self.color = input_color

    def printGender(self):
        print self.gender

    def printColor(self):
        print self.color


li_lei = Human('male', 'black')  # 创建Human类的对象li_lei，对象性质（gender,color）分别为(male,black)，为对象li_lei特有的性质
print li_lei.gender  # 调用对象性质
print li_lei.color
li_lei.printGender()  # 通过调用对象的方法来调用对象性质
li_lei.printColor()

# 实用内置函数
print "\ndir()用来查询一个类或者对象所有属性和方法："
print dir(Human)  # 查看Human类所拥有的所有属性和方法
print dir(li_lei)  # 查看对象li_lei所拥有的所有属性和方法

# print help(list)，help()用来查询说明文档


# 特殊运算方法
print "\n__add__这样的叫做特殊方法（下划线，下划线）："
print "\n自定义“-”方法："


class superList(list):
    def __sub__(self, b):
        a = self[:]  # 这里，self是supeList的对象。由于superList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象
        b = b[:]  # 将传入参数列表b全部赋值给b
        while len(b) > 0:
            element_b = b.pop()  # pop()函数用于移除列表中的一个元素（默认为最后一个元素），并返回该元素的值
            if element_b in a:  # 判断列表b中的该元素是否存在于列表a
                a.remove(element_b)  # 如果Ture则在列表a中移除此元素
        return a


print superList([1, 2, 3]) - superList([3, 4])

# 词典
print "\n词典："
print "\n创建词典："
dic = {'Tom': 25, 'Sam': 53, 'Jam': 85}
print type(dic)
print dic
# 修改词典dic中Tom键对应的值
print dic['Tom']
dic['Tom'] = 30
print dic

# 构建一个空词典
dic = {}
print dic
# 通过引用一个新的键来对新元素赋值
dic['lilei'] = 99
print dic

# 词典元素的循环调用
print "\n词典元素的循环调用："
dic = {'张三': 1, '李四': 2, '王五': 3, '赵六': 4}
for key in dic:
    print dic[key]

# 词典的常用方法
print "\n词典的常用方法："
dic_new = {'M1': 1, 'M2': 6, 'M3': 3, 'M4': 4, 'M5': 5}
# print dic_new.keys()                # 返回dic_new所有的键，无序的
# print dic_new.values()              # 返回dic_new所有的值，按照dic_new.keys()的顺序输出

# 按顺序输出字典dic_new中的内容
y = dic_new.keys()  # 将字典dic_new()存入列表y
y.sort()  # 将列表y按顺序排列，但是会改变原有列表
print "\n输出dic_new：\n", dic_new.values()  # 返回dic_new所有的值
print "顺序输出字典dic_new："  # 根据key的值进行排序，请见M2：6
for i in range(y.__len__()):  # 根据列表y的长度（字典的长度）顺序输出字典dic_new的键和值
    print y[i], dic_new[y[i]]

print "\n输出dic_new所有的值：\n", dic_new.values()  # 返回dic_new所有的值
print "顺序输出dic_new所有的值："
dic_list_1 = dic_new.values()
dic_list_1.sort()
print dic_list_1
print "\n输出dic_new所有的元素：\n", dic_new.items()  # 返回dic_new所有的元素
print "顺序输出dic_new所有的元素："  # 根据key的值进行排序，请见M2：6
dic_list_2 = dic_new.items()
dic_list_3 = sorted(dic_list_2)
print dic_list_3
# 删除字典元素
dic_list_4 = deepcopy(dic_new)
# 涉及到深复制和浅复制问题，对浅复制的主体和复制体进行的操作是等同的，删除任何字典中的元素都会导致主体和所有的复制体产生变化
# 但是不会对深复制体产生影响

print "\ndic_list_4的元素情况为：", dic_list_4.items()

del dic_list_4['M3']
print "删除后的dic_list_4的元素情况为：", dic_list_4.items()
# 查询字典中的元素总数
dic_list_5 = dic_new
print dic_new
print "\ndic_list_5的元素总数为：", len(dic_list_5), "个。"

# 列表的排序
print "\n列表的排序："
print "利用.sort()方法对列表进行排序："
list_1 = dic_new.keys()  # 将字典dic_new()存入列表list_1
print "原列表list_1：", list_1
list_1.sort()  # 将列表list_1按顺序排列，但是会改变原有列表
print "sort()方法改变后的列表list_1：", list_1  # 输出列表list_1

print "\n利用sorted()方法对列表进行排序："
list_2 = dic_new.keys()  # 将字典dic_new()存入列表list_2
print "原列表list_2：", list_2
list_3 = sorted(list_2)  # 将列表list_2按顺序排列，存入列表list_3，列表list_2不会改变原有列表
print "使用sorted()方法后的列表list_3：", list_3
print "再次输出list_2：", list_2  # 输出列表list_2

# 而且list.sort()方法仅被定义在list中，相反地sorted()方法对所有的可迭代序列都有效。

# 列表排序的复杂应用：
print "\n按年龄对列表student_info进行排序："
student_info = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
print sorted(student_info, key=lambda student_age: student_age[0])
# 按照学生年龄对列表进行排序，lambda为匿名函数，作用是将函数公式化，该句作用是建立一个名为lambda的方法，参数是student_age，返回值为student_age[2]

# 文本文件的输入输出
# 创建文件对象
print "\n创建文件对象："
f = open("test.txt", "r")
# 读取文件内容
if os.path.isfile('./test.txt'):  # 判断是否存在test.txt文档
    if os.path.getsize('./test.txt'):  # 判断文档test.txt中是否有内容
        file_name = f.name  # 读取文档名称
        print "文件名称：", file_name
        content = f.readlines()  # 将文档内容逐行存入列表centent[]，一行为一个元素
        print "文件内容为："
        for i in range(content.__len__()):  # 逐行打印
            print i + 1, "：", content[i].strip('\n')  # 去除每个元素的‘\n’属性
        f.close()  # 关闭文件，每次操作完成后都需要关闭文件以防止误操作和内存泄露
    else:
        print "该文档无内容！"
else:
    print "无此文档！"

# 引入模块
print "\n引入模块Python_Def，并调用方法laugh()："
for i in range(4):
    Python_Def.laugh(c=1, a=3, b=2)  # 参数传递可不按照位置，使用关键字进行定位

print "\n直接调用方法laugh()："
for i in range(4):
    laugh(1, c=2, b=3)  # 使用from Python_Def import laugh 引用，故可以直接使用laugh()方法

# 参数默认值
print "\n参数默认值："


def default(a, b, c=10):  # 参数c默认设置为10，故结果为15
    return a + b + c


print (default(3, 2))

# 包裹传递
print "\n包裹位置传递："


def packet_1(*parameter):  # 通过*定义包裹位置传递，不用声明参数个数
    print type(parameter)
    for i in range(parameter.__len__()):
        print parameter[i]


packet_1(1, 2, 3, 4)

print "\n包裹关键字传递："


def packet_2(**parameter):  # 通过*定义包裹关键字传递，不用声明参数个数
    print type(parameter)  # 关键字传递一般按照字典传递
    print parameter


packet_2(b=1, a=2, c=3, d=4)

print "\n解包裹："


def packet_3(a, b, c):  # 正常定义函数
    print a, b, c


args = (1, 2, 3)  # 传递为列表时，可以使用包裹位置传递
packet_3(*args)  # 如果不加*会被认为是只传1个参数，报错提示传参有误

args_dic = {'a': 1, 'b': 2, 'c': 3}  # 传递为字典时，可以使用包裹关键字传递
packet_3(**args_dic)

# 在定义或者调用参数时，参数的几种传递方式可以混合。但在过程中要小心前后顺序。基本原则是：先位置，再关键字，再包裹位置，再包裹关键字，并且根据上面所说的原理细细分辨。
# 注意：请注意定义时和调用时的区分。包裹和解包裹并不是相反操作，是两个相对独立的过程。

# 字典映射
print "\n字典映射："


def zero():
    print "0"


def one():
    print "1"


def two():
    print "2"


def defaul():
    print "None"


def test(argument, noen=None):
    switcher = {
        0: zero,
        1: one,
        2: two,
        noen: defaul(),
    }
    func = switcher.get(argument, lambda: "None")
    return func()


test(3)
