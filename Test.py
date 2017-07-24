#单元测试与文本测试
#
#如果你听说过“测试驱动开发”(TDD)，单元测试就不陌生。单元测试是用来对一个模块，
#一个函数或者一个类进行正确性检验的测试工作。以测试为驱动的开发模式最大的好处
#就是确保一个程序模块的行为符合我们设计的测试用例。在将来修改的时候，可以极大
#程度地保证该模块行为仍然是正确的。编写单元测试时，我们需要编写一个测试类，从
#unittest.TestCase继承。以test开头的方法就是测试方法，不以test开头的方法不被认
#为是测试方法，测试的时候不会被执行。对每一类测试都需要编写一个test_xxx()方法。
#由于unittest.TestCase提供了很多内置的条件判断。我们只需要调用这些方法就可以
#断言输出是否是我们所期望的。最常用的断言就是assertEqual().另一种重要的断言就是
#期待抛出指定类型的Error。一旦编写好单元测试，我们就可以运行单元测试。最简单的
#运行方式是在文件的最后加上两行代码
#if __name__=='__main__':
#	unittest.main()
#另一种方法是在命令行通过参数-m unittest直接运行单元测试。这是推荐的做法，因为
#这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。
#
#	
#可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调
#用一个测试方法的前后分别被执行。
#
#	
#单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
#单元测试的测试用例要覆盖常用的输入组合，边界条件和异常
#单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
#单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。			

class Dict(dict):
	
	'''
	Simple dict but also support access as x.y style

	>>> d1=Dict()
	>>> d1['x']=100
	>>> d1.x
	100
	>>> d1.y=200
	>>> d1['y']
	200
	>>> d2=Dict(a=1,b=2,c='3')
	>>> d2.c
	'3'
	>>> d2['empty']
	Traceback (most recent call last):
		...
	KeyError:'empty'
	>>> d2.empty
	Traceback (most recent call last):
		...
	AttributeError:'Dict' object has no attribute 'empty'
	'''
	def __init__(self,**kw):
			super().__init__(**kw)
	def __getattr__(self,key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute'%s'"%key)
	def __setattr__(self,key,value):
		self[key]=value

d=Dict(a=1,b=2)
print(d['b'])
print(d.a)
import unittest
class TestDict(unittest.TestCase):
	def test_init(self):
		d=Dict(a=1,b='test')
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))
	def test_key(self):
		d=Dict()
		d['key']='value'
		self.assertEqual(d.key,'value')
	def test_attr(self):
		d=Dict()
		d.key='value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'],'value')
	def test_keyerror(self):
		d=Dict()
		with self.assertRaises(KeyError):
			value=d['empty']
	def test_attrerror(self):
		d=Dict()
		with self.assertRaises(AttributeError):
			value=d.empty
	def setUp(self):
		print('setUp...')
	def tearDown(self):
		print('tearDown...')


#if __name__=='__main__':
#	unittest.main()
#


#文档测试：Python内置的“文档测试”(doctest)模块可以直接提取注释中的代码并执行
#测试。doctest严格按照python交互式命令行的输入和输出来判断测试结果是否正确。
#只有测试异常的时候，可以用...表示中间一大段烦人的输出。doctest非常有用，不但
#可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，就可以自动把包含
#doctest的注释提取出来。用户看文档的时候，同时也看到了doctest。
import re
m=re.search('(?<=abc)def','abcdef')
print(m.group(0))
if __name__=='__main__':
    import doctest
    doctest.testmod()