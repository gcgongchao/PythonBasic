#循环
#Python的循环有两种：(1)一种是for...in循环，依次把list或tuple中的每个元素迭代出来，
#如代码清单1。(2)第二种循环是while循环，只要条件满足，就不断循环，条件不满足就退出
#循环,如代码清单2。
#Python提供了一个range()函数，可以生成一个整数序列，再通过list函数可以转换
#为list，如代码清单3
#break：在循环中，故障break语句可以提前退出循环。
#continue：在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
#
#循环是让计算机做重复任务的有效的办法
#break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始
#下一轮循环。这两个语句通常都必须配合if语句使用。要特别注意，不要滥用break和continue语
#句，一般情况下，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。
#


#代码清单1
names = ['Michael','Bob','Tracy']
for name in names:
	print(name)

#代码清单2：
sum=0
n=99
while n>0:
	sum=sum+n
	n=n-2
print(sum)
#代码清单3：
print(list(range(5)))