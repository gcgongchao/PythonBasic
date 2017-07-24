#函数式编程
#函数式Python內建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，
#就可以把复杂任过程务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就
#是面向过程的程序设计的基本单元。
#
#而函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向
#过程的程序设计，但其思想更接近数学计算。
#我们首先要搞明白计算机(Computer)和计算(Compute)的概念。
#在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，
#汇编语言是最贴近计算机的语言。而计算则指数学意义上的计算，越是抽象的计算，离计算机
#硬件越远。对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，
#比如C语言；越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言。
#
#函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，
#因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副
#作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能
#得到不同的输出，因此，这种函数是有副作用的。
#
#函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数。
#Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程
#言。
###################################################
#高阶函数：把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的
#	编程范式。
#函数本身也可以赋值给变量，即：变量可以指向函数。注意：函数名也是变量。
#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数
#，这种函数就称之为高阶函数。编写高阶函数，就是让函数的参数能够接收别的函数。

f=abs
print(f(-10))
def add(x,y,f):
	return f(x)+f(y)
print(add(-10,-20,f))

#map/reduce:
#Python內建了map()和reduce()函数。我们先看map。map()函数接收两个参数，一个是函数，一个
#是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
#reduce:reduce把一个函数作用在一个序列[x1,x2,x3,...]上，这个函数必须接收两个参数，reduce
#把结果继续和序列的下一个元素做累积计算。


def f(x):
	return x*x
print(list(map(f,[1,2,3,4,5,6,7,8,9])))
print(list(map(str,[1,2,3,4,5,6,7,8,9])))

from functools import reduce
def add(x,y):
	return x+y
print(reduce(add,[1,3,5,7,9]))

def fn(x,y):
	return x*10+y
print(reduce(fn,[1,3,5,7,9]))

def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
print(reduce(fn,map(char2num,'12345678')))


l=['adam','LISA','barT']

def name(_name):
	return _name.capitalize()
print(name('tESt'))
print(list(map(name,l)))

def prod(x,y):
	return x*y
print(reduce(lambda x,y:x*y,[1,2,3,4,5,10]))

#def str2float(s):
#	def generate_float(s):
#		index=10
#		if(s.equal('.')):
#			index=0.1
#		
#	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':'.'}[s]
#print(list(map(str2float,'123.456')))




#filter:Python内建的filter()函数用于过滤序列。和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。注意到filter()函数返回的是一个Iterator，
# 也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
# filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，
# 才会真正筛选并每次返回下一个筛出的元素。
def is_odd(n):
	return n%2==1
print(list(filter(is_odd,[1,2,4,5,6,9,10,15])))

def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty,['A','','B',None,'C',' '])))


#sorted:Python内置的sorted()函数可以进行排序,sorted()函数也是一个高阶函数，它还可以接收一个Key函数来实现自定义的排序。
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。要进行反向排序，不必改动key函数，
# 可以传入第三个参数reverse=True。sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
print(sorted([1,4,5,2,3]))
print(sorted((11,-4,-5,2,3),key=abs))



#返回函数：高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
#闭包：注意到返回的函数在其定义内部引用了局部变量args,所以，当一个函数返回了一个函数后，
# 其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变。一个函数可以返回一个计算结果，也可以返回一个函数。
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum
print(lazy_sum(1,3,5,7,9)())
f1=lazy_sum(1,3,5,7,9)
f2=lazy_sum(1,3,5,7,9)
print(f1==f2)



def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1,f2,f3=count()
print(f1())
print(f2())
print(f3())


def count1():
	def f(j):
		def g():
			return j*j
		return g
	fs=[]
	for i in range(1,4):
		fs.append(f(i))
	return fs

f1,f2,f3=count1()

print(f1())
print(f2())
print(f3())

#匿名函数：当我们在传入函数时，有些时候，不需要显示地定义函数，直接传入匿名函数更方便。
# 关键字lambda表示匿名函数，冒号前面的表示函数参数。匿名函数有个限制，就是只能有一个表达式，
# 不用写return,返回值就是该表达式的结果。用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
# 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数。
# 同样，也可以把匿名函数作为返回值返回。Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。

print(list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])))

f=lambda x:x*x
print(f(10))
def build(x,y):
	return lambda:x*x+y*y
print(build(3,4)())

#装饰器：由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
# 函数对象有一个__name__属性，可以拿到函数的名字。在代码运行期间动态增加功能的方式，称之为“装饰器(Decorator)”。
# 本质上，decorator就是一个返回函数的高阶函数。在面向对象(OOP)的设计模式中，decorator被称为装饰模式。
# OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。
# Python的decorator可以用函数实现，也可以用类实现。decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
import functools


def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):#参数定义为*args,**kw主要是为了让函数可以接受任意参数的调用
		print('call %s():'%func.__name__)
		return func(*args,**kw)
	return wrapper

@log
def now():
	print('2015-3-25')
f=now
print(now.__name__)
print(f.__name__)#要有两个下划线
print(now())

def log1(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s():'%(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
@log1('test')
def now1():
	print('2017-07-07')
d=now1()
print(d)
print(now1.__name__)



#偏函数：Python的functools模块提供了很多有用的功能，其中一个就是偏函数(Partial function)。
# 要注意，这里的偏函数和数学意义上的偏函数不一样。在介绍函数参数的时候，我们讲到，通过设定参数的默认值，
# 可以降低函数调用的难度。而偏函数也可以做到这一点。int()函数可以把字符串转换为整数，当仅传入字符串时，
# int()函数默认按十进制转换。int()函数还额外提供了base参数，默认值为10。如果传入base参数，就可以做N进制的转换。
# 简单说一下functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，
# 调用这个新函数会更简单。当函数的参数个数太多，需要简化时，使用fuctools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

print(int('12345'))
print(int('12345',base=8))
print(int('12345',16))

int2=functools.partial(int,base=2)
int2('1000')


