# coding=utf-8
# 打印&赋值
import time

import datetime
import types

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
    c = a**2 + b**2
    return c


# 调用函数square_sum（a,b）
print square_sum(1,2)

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
    have_feather = True            # 是否有羽毛
    way_of_reproduction = 'egg'     # 生殖方式

    def move(self, dx, dy):        # 定义鸟的移动方法
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


class Chicken(Bird):        # 定义鸡类，继承了鸟类的是否有羽毛、生殖方式属性，自身增加了行动方式、是否出现在KFC属性
    way_of_move = 'walk'
    possible_in_KFC = True


class Oriole(Bird):         # 定义黄鹂类，继承了鸟类的是否有羽毛、生殖方式属性，自身增加了行动方式、是否出现在KFC属性
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

li_lei = Human('male', 'black')     # 创建Human类的对象li_lei，对象性质（gender,color）分别为(male,black)，为对象li_lei特有的性质
print li_lei.gender                # 调用对象性质
print li_lei.color
li_lei.printGender()                # 通过调用对象的方法来调用对象性质
li_lei.printColor()

# 实用内置函数
print "\ndir()用来查询一个类或者对象所有属性和方法："
print dir(Human)                    # 查看Human类所拥有的所有属性和方法
print dir(li_lei)                   # 查看对象li_lei所拥有的所有属性和方法

# print help(list)，help()用来查询说明文档


# 特殊运算方法
print "\n__add__这样的叫做特殊方法（下划线，下划线）："
print "\n自定义“-”方法："


class superList(list):
    def __sub__(self, b):
        a = self[:]                 # 这里，self是supeList的对象。由于superList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象
        b = b[:]                    # 将传入参数列表b全部赋值给b
        while len(b) > 0:
            element_b = b.pop()     # pop()函数用于移除列表中的一个元素（默认为最后一个元素），并返回该元素的值
            if element_b in a:      # 判断列表b中的该元素是否存在于列表a
                a.remove(element_b)     # 如果Ture则在列表a中移除此元素
        return a

print superList([1, 2, 3]) - superList([3, 4])

# 判断闰年的函数
print "\n判断闰年的函数："


def isRUN(data):
    year = round(int('data[0:3]'))
    month = round(int('data[4:5]'))
    day = round(int('data[7:8]'))

    if year % 4 == 0:
        print 'Ture'
        print('%d.%d.%d 是闰年'%(year, month, day))
    else:
        print 'False'
        print('%d.%d.%d 不是闰年' % (year, month, day))

# data = input("请输入日期：")
# isRUN(data)

# 获取时间
# import time
# localtime = time.asctime(time.localtime(time.time()))
# print "time is : ", localtime

# data_input = raw_input('请输入日期，格式为yyyy-mm-dd : \n')
# data_time = time.strptime(data_input, "%Y-%m-%d")
# y, m, d = data_time[0:3]
# print (datetime.datetime(y, m, d))


# 判断用户输入年份是否为闰年
print "\n判断用户输入的日期是否为闰年的函数："


# noinspection PyGlobalUndefined
def input_date():                       # 输入数据
    global date
    date = raw_input("请输入想要查询的日期，格式为：年-月-日（如：2017-01-01）:\n")
    return date


# noinspection PyBroadException
def dateConfirmation():                 # 处理输入的日期
    try:
        date1 = input_date()
        print '你输入的日期是：',date1
        datetime.datetime.strptime(date1, format_date)
        year = time.strptime(date1, "%Y-%m-%d")
        newYear = "%s" % year.tm_year
        return newYear
    except:
        print "日期格式输入错误，请重新输入：\n"
        input_date()


def judge(year=None):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print year, '是闰年'
    else: print year, '不是闰年'


# noinspection PyGlobalUndefined
global format_date
format_date = "%Y-%m-%d"


def isLeap_year():
    year = dateConfirmation()
    print '年份是：', year
    if type(year) is types.IntType:
        judge(year)
    else:
        year = int(year)
        judge(year)
    return True

isLeap_year()                          # 运行判断闰年函数


