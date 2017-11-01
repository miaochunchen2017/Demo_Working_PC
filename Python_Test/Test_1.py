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
print "5 = 6 ?   ==>  ", 5 == 6;
print "8 != 8 ?   ==>  ", 8 != 8;
print "3 < 3 ?   ==>  ", 3 < 3;
print "3 <= 3 ?   ==>  ", 3 <= 3;
print "5 in [1,3,5] ?   ==>  ", 5 in [1, 3, 5];
print '"Mcc" is "Mcc" ?   ==>  ', "Mcc" is "Mcc"
print '"Mcc" is not "ZMR" ?   ==>  ', "Mcc" is not "ZMR"

