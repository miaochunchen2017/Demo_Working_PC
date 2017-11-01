#coding=utf-8
#打印&赋值
print "\n打印&赋值："
#打印
print 'Hello World!';
#赋值
a = 10;
print a, type(a);
a=1.3
print a, type(a);

#序列
print "\n序列："
#类型为tuple，无法更改
s1 = (2, 1.3, 'love', 5.6, 9, 12, False);
#类型为list，可以更改
s2 = [True, 5, 'smile'];
print s1, type(s1);
print s2, type(s2);
s2[1] = 4;
print s2,type(s2);
s3 = [1, [3, 4, 5]];
print s3[1][2];
print "数组原貌:", s1;
#从开始到下标4
print "从开始到下标4:", s1[:4];
#从开始到结束，每隔2个元素显示
print "从开始到结束，每隔2个元素显示:", s1[::2];
#从开始到结束，倒序打印
print "从开始到结束，倒序打印:", s1[::-1];
#序列最后一个元素
print "最后一个元素:", s1[-1];
#序列倒数第三个元素
print "倒数第三个元素:", s1[-3];

#字符串
print "\n字符串："
str = 'Mcc is a SUPERMAN.';
print "字符串str为:", str;
#显示第4位需要“str[3：”，而显示第8位则可以“str[3:8]”
print "字符串str中的第4位到第8位字符为:", str[3:8];

#基础运算
print "\n基础运算："
print "1 + 9 =", 1 + 9;
print "1.3 - 4 =", 1.3 - 4;
print "3 * 5 =", 3 * 5;
print "4.5 / 1.5 =", 4.5 / 1.5;
print "3 ** 2 =", 3 ** 2;
print "10 % 5 =", 10 % 5;

#判断
print "\n判断："
print "5 = 6 ?   ==>  ", 5 == 6;
print "8 != 8 ?   ==>  ", 8 != 8;
print "3 < 3 ?   ==>  ", 3 < 3;
print "3 <= 3 ?   ==>  ", 3 <= 3;
print "5 in [1,3,5] ?   ==>  ", 5 in [1, 3, 5];
print '"Mcc" is "Mcc" ?   ==>  ', "Mcc" is "Mcc"
print '"Mcc" is not "ZMR" ?   ==>  ', "Mcc" is not "ZMR"

#逻辑运算，True/False之间的运算
print "\n逻辑运算："
# and , “与”运算，两者都为真才是真
print "True and True   ==>  ", True and True
print "True and False   ==>  ", True and False
# or , “或”运算，其中之一为真即为真
print "True or False   ==>  ", True or False
print "True or False or False   ==>  ", True or False or False
# not , “非”运算，取反
print "not True   ==>  ", not True
#结合起来，比如：
print "5 = 6 or 3 >= 3 'True or False ?'  ==>  ", 5 == 6 or 3 >= 3

#缩进：if条件语句
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




