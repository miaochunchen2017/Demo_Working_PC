# coding=utf-8
# 判断用户输入年份是否为闰年
import datetime
import os
import time
import types


# print "\n判断用户输入的日期是否为闰年的函数："


# noinspection PyGlobalUndefined
def input_date():  # 输入数据
    global date
    date = raw_input("请输入想要查询的日期，格式为：年-月-日（如：2017-01-01）:\n")
    return date


# noinspection PyBroadException
def dateConfirmation():  # 处理输入的日期
    try:
        date1 = input_date()
        print '你输入的日期是：', date1
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
    else:
        print year, '不是闰年'


# noinspection PyGlobalUndefined
global format_date
# noinspection PyRedeclaration
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


# isLeap_year()                          # 运行判断闰年函数

# 定义调用DEMO


def laugh(a, b, c):
    print a, b, c


# 建立record.txt文档，并写入内容


def searchForFile():
    # 检查文件，如果存在则打开，不存在则创建该文件
    file_name = raw_input("请输入要查找的文件名：\n")
    is_exist = os.path.isfile('./' + file_name)
    if is_exist:
        file_1 = open(file_name, 'a+')
        print "文件存在，已打开文件：", file_1.name
    else:
        file_YN = raw_input("文件不存在，请问是否创建文件（Y/N）：\n")
        if file_YN == 'Y' or file_YN == 'y':
            file_2_name = raw_input("文件名称为：\n")
            file_2 = open(file_2_name, 'a+')
            print "文件已创建：", file_2.name
        else:
            print "欢迎使用！"


searchForFile()
