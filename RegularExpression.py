#正则表达式：正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串定义一个规则，
# 凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法。在正则表达式中，如果直接给出字符，就是精确匹配。
# 用\d可以匹配一个数字，\w可以匹配一个字母或数字。.可以匹配任意字符。要匹配变长的字符，在正则表达式中，
# 用*表示任意个字符(包括0个),用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n-m个字符。
# \s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格。要做更精确的匹配，可以用[]表示范围，
# 比如：[0-9a-zA-Z]可以匹配一个数字，字母或者下划线；[0-9a-zA-Z\_]+可以匹配至少由一个数字，
# 字母或者下划线组成的字符串；[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或者下划线开头，后接任意个由一个数字，
# 字母或者下划线组成的字符串，也就是Python合法的变量。[a-zA-Z\_][0-9a-zA-Z\_]{0,19}更精确地限制了变量的长度是1-20个字符；
# A|B可以匹配A或B，^表示行的开头，^\d表示必须以数字开头。$表示行的结束，\d$表示必须以数字结尾。


#re模块:Python提供了re模块，包含所有正则表达式的功能。
#分组：除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组(Group)。
#贪婪匹配：最后需要特别指出的是，正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。

#编译：当我们在Python中使用正则表达式时，re模块内部会干两件事情：（1）编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
# （2）用编译后的正则表达式去匹配字符串。如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，
# 接下来重复使用时就不需要编译这个步骤了，直接匹配。

import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.split(r'[\s\,\;]+','a,,,,b;;;  c   d'))
t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())
m1=re.match(r'^(\d+?)(0*)$','1000029000');#加个?就可以让\d+采用非贪婪匹配。
print(m1)
print(m1.groups())

re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('010-12345').groups())
print(re_telephone.match('010-8086').groups())

