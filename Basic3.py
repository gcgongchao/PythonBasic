#字符串也是一种数据类型，但是，字符串比较特殊的是还有一个编码问题。因为字符串
#只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。因为计算机只
#能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。最早的计算机在
#设计时采用8个bit作为一个字节byte，所以，一个字节能表示的最大的整数就是255，如
#果要表示更大的整数，就必须用更多的字节。由于计算机是美国人发明的，因此，最早只
#有127个字符被编码到计算机里，也就是大小写英文字母，数字和一些符号，这个编码表被
#称为ASCII编码。但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能
#和ASCII编码冲突，所以，中国制定了GB2312编码，用来把中文编进去。你可以想得到的_JIS是，
#全世界有上百种语言，日本把日文编导Shift_JIS里，韩国把韩文编到Eur-kr里，各国有各国
#的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。
#因此，Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。
#
#
#Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符，
#就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode。
#
#ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。
#本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个
#Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常
#是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，
#用UTF-8编码就能节省空间。
#
#现在计算机系统通用的字符编码工作方式：在计算机内存中，统一使用Unicode编码，当需要保存到
#硬盘或者需要传输的时候，就转换为UTF-8编码。
#
#Python对bytes类型的数据用带b前缀的单引号或双引号表示:x=b'ABC',要注意区分'ABC'和b'ABC',前者
#是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。以Unicode表示的
#str通过encode()方法可以编码为指定的bytes。纯英文的str可以用ASCII编码为bytes，内容是一样的，
#含有中文的str可以用UTF-8编码为bytes.含有中文的str无法用ASCII编码，因为中文编码的范围超过了
#ASCII编码的范围，Python会报错。在bytes中，无法显示为ASCII字符的字节，用\x##显示。反过来，如
#果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode方
#法。
#要计算str包含多少个字符，可以用len()函数。len()()函数计算的是str的字符数，如果换成bytes,len()
#函数就计算字节数。1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用
#1个字节。在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终
#坚持使用UTF-8编码对str和bytes进行转换。由于Python源代码也是一个文本文件，所以
#当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python
#解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
##!/usr/bin/env python3
##-*- coding:utf-8 -*
#第一行注释是为了告诉linux/os x系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的
#中文输出可能会有乱码。注意：申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须
#并且要确保文本编辑器正在使用UTF-8 without BOM编码。如果.py文件本身使用UTF-8编码，并且也
#申明了# -*- coding: utf-8 -*-,打开命令提示符测试就可以正常显示中文。
#
#格式化：
#最后一个常见的问题是如何输出格式化的字符串。在Python中，采用的格式化方式和
#c语言是一致的，用%实现。你可能猜到了，%运算符就是用来格式化字符串的。在字符串内部，
#%s表示用字符串替换，%d表示用整数替换，有几个%？占位符，后面就跟几个变量或者值，顺序
#要对应好，如果只有一个%？，括号可以省略。常见的占位符有：%d——整数；%f——浮点数；
#%s——字符串；%x——十六进制整数 。其中，格式化整数和浮点数还可以指定是否补0和整数与小数
#的位数.如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串。
#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%。
# Python 3的字符串使用Unicode，直接支持多语言。str和bytes互相转换时，需要指定编码，
# 最常用的编码是UTF-8。Python当然也支持其他编码方式，比如把Unicode编码成GB2312，
# 但这种方式纯属自找麻烦，如果没有特殊业务要求，请牢记仅使用UTF-8编码。
print('包含中文的str')
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
#print('中文'.encode('ascii'))
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('ABC'))
print(len('中文'))
print(len('中文'.encode("utf-8")))
print('中文测试显示')
print('%02d-%02d'%(3,1))
print("%.2f"%3.1415926)
print('Age:%s..Gender:%s'%(25,True))
print('growth rate: %d %%'%7)
s1=72
s2=85
r=(s2-s1)/s1*100
print('result:%.1f%%'%r)
print
