#条件判断：
#计算机之所以能做很多自动化的任务，因为它可以自己做条件判断。
#elif 是else if的缩写.
#if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句
#执行后，就忽略掉剩下的elif和else。如代码清单3
#if判断条件还可以简写，比如代码清单4：
#int()可以把str转换为整数,当然str如果不是纯数字组成的会报错，如代码清单5




#代码清单1
age=20
if age>=19:
	print(("your age is %d"%age))
	print('adult')
else:
	print("your age is %d"%age)
	print("teenager")
#代码清单2
age1=3
if age1>=18:
	print('adult1')
elif age1>=6:
	print('teenager1')
else:
	print('kid1')
#代码清单3
age2=20
if(age2>=6):
	print('teenager2')
elif age2>=18:
	print('adult2')
else:
	print('kid2')

#代码清单4
x=1
if x:
	print('True')

#代码清单5：
s=input('birth:')
birth=int(s)
if birth<2000:
	print("00前")
else:
	print('00后')