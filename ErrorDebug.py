#错误，调试和测试：Python内置了一套异常处理机制，来帮助我们进行错误处理。此外，我们也需要跟踪程序的执行，
# 查看变量的值是否正确，这个过程称为调试。Python的pdb可以让我们以单步方式执行代码。
# Python内置了一套try...except...finally...的错误处理机制。当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
# 如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，
# 如果有finally语句块，则执行finally语句块。如果没有错误发生，可以在except语句块后面加一个else，
# 当没有错误发生时，会自动执行else语句。Python的错误其实也是class，所有的错误类型都继承自BaseException,
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。Python内置的logging模块可以
# 非常容易地记录错误信息。raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中的raise一个Error，
# 还可以把一种类型的错误转化为另一种类型。
import logging
try:
	print('try....')
	r=10/0
	print('result:',r)
except Exception as e:
	print('except:',e)
	logging.exception(e)
finally:
	print('finally....')
print('END')


class FooError(ValueError):
	pass
def foo(s):
	n=int(s)
	if n==0:
		raise FooError('invalid value :%s'%s)
	return 10/n

#foo('0')


#调试：在Python中调试分为以下手段：（1）print(2)assert(3)logging(4)pdb(5)pdb.set_trace(6)IDE。
# 断言：凡是用print来辅助查看的地方，都可以用断言(assert)来替代。如果断言失败，assert语句本身就会抛出AssertionError。
# logging不会抛出错误，而且可以输出到文件。logging.info()就可以输出一段文本。
# logging允许你指定记录信息的级别，有debug，info,warning,error等几个级别。
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方。
def foo_debug(s):
	n=int(s)
	assert n!=0,'n is zero!'
	return 10/n
def main():
	foo_debug('0')
#main()
logging.basicConfig(level=logging.INFO)
s='0'
n=int(s)
logging.info('n=%d'%n)
print(10/n)




