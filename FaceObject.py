#面向对象编程：面向对象编程(Object Oriented Programming),简称OOP，是一种程序设计思想。
#OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

#面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序
#设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。
#而面向对象的程序设计把计算机程序视为一组对象的组合，而每个对象都可以接收其他对象发过来
#的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。给对象发消息
#实际上就是调用对象对应的关联函数，我们称之为对象的方法。

#在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是
#面向对象中的类(Class)的概念。
#
#面向对象的设计思想是抽象出Class，根据Class创建Instance。面向对象的抽象程度又比函数要高，
#因为一个Class既包含数据，又包含操作数据的方法。
#
class Student(object):
		name='test'
		school='ahut'
		def __init__(self,name,score):
			self.name=name
			self.score=score

		def print_score(self):
			print('%s:%s'%(self.name,self.score))

		def get_grade(self):
			if self.score>=90:
				return 'A'
			elif self.score>=60:
				return 'B'
			else:
				return 'C'


#bart=Student('Bart Simpson', 59)
#lisa=Student('Lisa Simpson', 87)
#bart.print_score()
#lisa.print_score()
#print(bart.get_grade())
#print(lisa.get_grade())
#bart.age=8
#print(bart.age)
#print(lisa.age)


#类和实例：面向对象最重要的概念就是类(Class)和实例(Instance)，必须牢记类是抽象的模板，而
#实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
#class 后面紧接着是类名，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继
#承下来的，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。由于类
#可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
#通过定义一个特殊的__init__方法，在创建实例的时候，就把相关属性绑上去。注意：特殊方法"init"
#前后有两个下划线。注意__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在
#__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。有了__init__
#方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不
#需要传，Python解释器自己会把实例变量传进去。和普通的函数相比，在类中定义的函数只有一点不同
#，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通
#函数没有区别，所以，你仍然可以用默认参数，可变参数，关键字参数和命名关键字参数。要调用一个
#方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入。

#数据封装：面向对象编程的一个重要特点就是数据封装。
#类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
#方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；通过在实例上调用方
#法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
#
#和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都
#是同一个类的不同实例，但拥有的变量名称都可能不同。
#
#


#访问限制：在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，
#这样，就隐藏了内部的复杂逻辑。




class Animal(object):
	def run(self):
		print('Animal is running...')
	

class Dog(Animal):
	def run(self):
		print("Dog is running")
	def eat(self):
		print('Eating meat....')
class Cat(Animal):
	def run(self):
		print("Cat is running....")

dog=Dog()
dog.run()

cat=Cat()
cat.run()
#在Python中，任何类，最终都可以追溯到根类object。
#静态语言VS动态语言：对于静态语言(例如java)来说，如果需要传入Animal类型，
# 则传入的对象必须是Animal类型或者它的子类。否则，将无法调用run方法。
# 而对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证传入的对象有一个run方法就可以了。这就是动态语言的"鸭子类型"，
# 它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
# Python的“file-like object”就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
# 但是，许多对象，只要有read()方法，都被视为"file-like object"。许多函数接收的参数就是"file-like object"，
# 你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。



#继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，
# 也可以把父类不适合的方法覆盖重写。动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

class Timer(object):
	def run(self):
		print("Start....")


def run_twice(animal):
		animal.run()
		animal.run()

run_twice(Timer())

#获取对象信息：使用type()来判断对象的类型。types模块中定义了一些常量也可以做一些判断。
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list。
# 仅仅把属性和方法列出来是不够的，配合getattr(),setattr()以及hasattr(),我们可以直接操作一个对象的状态。
print(type(123))
print(type('str'))
print(type(None))
print(type(dog))
print(type(abs))
import types
def fn():
	pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

print(dir('ABC'))

#实例属性和类属性：由于Python是动态语言，根据类创建的实例可以任意绑定属性。
# 但是要注意，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，
# 因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
s=Student('t',90)
print(s.name,s.school)
print(Student.name)
del s.name
print(s.name)









