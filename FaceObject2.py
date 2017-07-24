#数据封装，继承和多态只是面向对象程序设计中最基础的3个概念。
# 在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。

#正常情况下，当我们定义了一个class，创建了一个class的实例后，
# 我们可以给实例绑定任何属性和方法，这就是动态语言的灵活性。但是给一个实例绑定的属性和方法，
# 对另一个实例是不起作用的。为了给所有实例都绑定方法和属性，可以给Class绑定方法和属性。
# 动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

class Student(object):
	pass
s=Student()
s.name='GeneralAndroid'
print(s.name)

def set_age(self,age):
	self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s)#给实例绑定一个方法
s.set_age(25)
print(s.age)

s1=Student()
#print(s1.name)

def set_score(self,score):
	self.score=score
Student.name="Class GeneralAndrod"
Student.set_score=set_score
Student.set_age=set_age
s2=Student()
s2.set_score(90)
s2.set_age(23)
print(s2.name)
print(s2.age)
print(s2.score)
s3=Student()
s3.set_score(80)
s3.set_age(24)
print(s3.name)
print(s3.age)
print(s3.score)


# __slots__：对于一个类我们不能随意添加属性，要做一定的限制。Python中提供了一个特殊的变量__slots__来进行限制能添加的属性。
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。除非在子类中也定义__slots__，
# 这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

class Techer(object):
		__slots__=('name','age')#用tuple定义允许绑定的属性名称
t=Techer()
t.name="Techer"
t.age=34
#t.score=99

#使用@property:Python内置的@property装饰器负责把一个方法变成属性调用。@property广泛应用在类的定义中，
# 可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

class StudentSecond(object):
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value<0 or value >100:
			raise ValueError('score must between 0~100!')
		self._score=value
	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self,value):
		self._birth=value
	@property
	def age(self):
		return 2017-self._birth



ss=StudentSecond()
ss.score=90
print(ss.score)
ss.birth=1992
print(ss.age)

#多重继承：通过多重继续，一个子类就可以同时获得多个父类的所有功能。在设计类的继承关系时，通常，主线都是单一继承下来的，
# 如果需要“混入”额外的功能，通过多重继承就可以实现，这种设计通常称之为MixIn。MixIn的目的就是给一个类增加多个功能，
# 这样，在设计类的时候，我们优先考虑通过多重继续来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。



#定制类：在Python中形如__XXX__的变量或者函数名是有特殊用途的，可以帮助我们定制类。
# __iter__:如果一个类想被用于for...in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环。相应的还有__getitem__(),__setitem__()，__delitem()等方法,
# 总之，通过这些方法，我们自己定义的类表现得和Python自带的list,tuple,dict没什么区别，这完全归功于动态语言的"鸭子类型",
# 不需要强制继承某个接口。__getattr__：在Python中，当调用不存在的属性时，Python解释器会试图调用__getattr__()来尝试获得属性。
# 注意：只有在没有找到属性的情况下，才调用__getattr__。__call__:.....Python的class允许定义许多定制方法，
# 可以让我们非常方便地生成特定的类。
class StudentThree(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'Student object(name:%s)'% self.name
	__repr__=__str__
print(StudentThree("General"))
s3=StudentThree('General')
s3


class Fib(object):
	def __init__(self):
		self.a,self.b=0,1
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>1000:
			raise StopIteration()
		return self.a


for n in Fib():
	print(n)

#枚举类：当我们需要定义常量时，一个办法是用大写变量通过整数来定义。
# 好处是简单，缺点是类型是int，并且仍然是变量。更好的办法是为这样的枚举类型定义一个class类型，然后，
# 每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能。如果需要更精确地控制枚举类型，
# 可以从Enum派生出自定义类。Enum可以 把一组相关常量定义在一个class中，且class不可变，而且成员可直接比较。
JAN=1
FEB=2
from enum import Enum
Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
for name,member in Month.__members__.items():
	print(name,'=>',member,',',member.value)
Sex=Enum('Sex',('Mal','Femal'))
for name,member in Sex.__members__.items():
	print(name,'=>',member,',',member.value)

print(Month.Jan.value)#value属性则是自动赋給成员的int常量，默认从1开始计数。
print(Sex.Femal)

from enum import Enum,unique

@unique
class Weekday(Enum):
	Sun=0
	Mon=1
	Tue=2
	Wed=3
	Thu=4
	Fri=5
	Sat=6
day1=Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1==Weekday.Mon)
print(day1==Weekday.Tue)
print(Weekday(1))
print(day1==Weekday(1))

for name,member in Weekday.__members__.items():
	print(name,'=>',member)

#使用元类：动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
from Hello import Hello
h=Hello()
h.hello()
print(type(Hello))
print(type(h))

