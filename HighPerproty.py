#切片:取一个list或tuple的部分元素是非常常见的操作，对这种经常取指定索引范围的操作，用循环十分繁琐，
# 因此，Python提供了切片（slice）操作符，大大简化了这种操作。

#迭代：如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# 在Python中，迭代是通过for...in来完成的，Python的for循环抽象程度要高于Java的for循环，
# 因为Python的for循环不仅可用在list或tuple上，还可以作用在其他可迭代对象上。
# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只有是可迭代对象，无论有无下标，都可以迭代。
# 在迭代dict时，由于dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
# 在Python中，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 那么如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判读。如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素树，这样就可以在for循环中同时迭代索引和元素本身。
# 任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。

#列表生成式：列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。range()

#生成器：通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成(),就创建了一个generator。
# 创建L和g的区别仅在于最外层的[]和(),L是一个list，而g是一个generator。我们创建了一个generator后，基本上永远不会调用next(),
# 而是通过for循环来迭代它，并且不需要关心StopIteration的错误。generator非常强大。如果推算的算法比较复杂，
# 用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，
# 而是一个generator。这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# 我们在用for循环来迭代generator函数的数据时，是拿不到generator的return语句的返回值的。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中。

#迭代器：我们已经知道，可以直接作用于for循环的数据类型有以下几种：一类是集合数据类型，如list,tuple,dict,set,str等；
# 一类是generator，包括生成器和带yield的generator function。这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。可以使用isinstance()判断一个对象是否是Iterator对象。
# 生成器都是Iterator对象，但list，dict，str虽然是Iterable，却不是Iterator。
# 把list，dict，str等Iterable变成Iterator可以使用iter()函数。
# 你可能会问，为什么list，dict，str等数据类型不是Iterator？这是因为Python的Iterator对象表示的是一个数据流，
# Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
# 可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。Iterator甚至可以表示一个无限大的数据流，
# 例如全体自然数。而使用list是永远不可能存储全体自然数的。

#凡是可作用于for循环的对象都是Iterable类型；凡是可作用于next()函数的对象都是Iterator类型，
# 它们表示一个惰性计算的序列；集合数据类型如list,dict,str等是Iterable但不是Iterator,
# 不过可以通过iter()函数获得一个Iterator对象。Python的for循环本质上就是通过不断调用next()函数实现的。
l=list(range(20))
print(l[0:4])
print(l[:3])
print(l[-4:-1])
print(l[::5])
print(l[:])


d={'a':1,'b':2,'c':3}
for key in d:
	print(key)

from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))



for i,value in enumerate(['A','B','C']):
	print(i,value)


for x,y,z in [(1,1,1),(2,4,3)]:
	print(x,y,z)

print('**********************')


print(list(range(1,11)))
print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x%2==0])
print([m+n for m in 'ABC' for n in 'XYZ'])
g=(x*x for x in range(11,21))
for n in g:
	print(n)


def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'
for x in fib(5):
	print(x)




def odd():
	
		print('step 1')
		yield 1
		print('step 2')
		yield 3
		print('step 3')
		yield 5
		return 'done'
	
	
o=odd()
print(next(o))
next(o)
next(o)
try:
	next(o)
except StopIteration as e:
	print('Generator return value:',e.value)
#print(next(o))
