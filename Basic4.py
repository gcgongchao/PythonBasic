#使用list和tuple
#list:Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加
#	和删除其中的元素。用索引来访问list中每一个位置的元素，记得索引是从0开始的
#	如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个
#	元素，以此类推。list是一个可变的有序表，所以，成可以往list中追加元素到末尾。
#	也可以把元素插入到指定的位置，要删除list末尾的元素，用pop()方法.要删除指定
#	位置的元素，用pop(i)方法，其中i是索引位置。要把某个元素替换成别的元素，可以
#	直接赋值给对应的索引位置。list里面的元素的数据类型也可以不同。list元素也可以
#	是另一个list.
#	
#tuple:	另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能
#修改,它没有append()，insert()这样的方法，其他获取元素的方法和list是一样的，但
#不能赋值成另外的元素。不可变的tuple有什么意义呢？因为tuple不可变，所以代码更安全。
#如果可能，能用tuple代替list就尽量用tuple.
#tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来。如果
#要定义一个空的tuple，可以写成()。但是，要定义一个只有1个元素的tuple，你需要加个逗号。
#这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，
#Python规定在显示只有1个元素的tuple时，会加一个逗号，，以免误解成数学计算意义上的括号。
#tuple一旦初始化之后不能改变指的是tuple的指向不变。
#
#list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。
classmates=['Michael','Bob','Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
#print(classmates[3])
print(classmates[-1])
classmates.append('Adam')
print(classmates)
classmates.insert(1,'Jack')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(0)
print(classmates)
classmates[1]='lalala'
print(classmates)
L=['Apple',123,True]
print(L)
s=['python','java',['asp','php'],'scheme']
print(s)
print(len(s))
t=(1,2)

print(t)
print(t[0])
print(t[-1])
#t[0]=3 #tuple不能更改元素的值
print(t)

s=(1)
print(s)
s1=(1,)
print(s1)
s2=(1,True,['first','second'])
print(s2)
s2[2][1]='thrid'
print(s2)