Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def check():
	name=input ('名字：')
	age=int(input('年龄：'))
	rs=print(f'{name}在',2018+(100-age),'年后100岁')
	return rs

>>> check()
名字：admin
年龄：20
admin在 2098 年后100岁
>>>
>>>
>>>
>>>
>>> def check_num():
	num=int(input('请输入一个整数：'))
	if num is None:
		print('请输入一个整数')
	elif num%2==1:
		print('你输入的是个奇数')
	else:
		print('你输入的是个偶数')

		
>>> check_num()
请输入一个整数：21
你输入的是个奇数
>>>
>>>
>>>
>>>
>>> list=['',{}]
>>> def check_null():
	for i in list:
		if list[1]:
			print('have')
		else:
			print('None')

			
>>> check_null()
None
None
>>>
>>>
>>> list=[(),0,False]
>>> all([list])
True
>>> all([[],''])
False
>>>
>>>
>>>
>>> lst=[(),'']
>>> def is_null():
	for x in list:
		return list[x]

	
>>> rs=filter(is_null,lst)
>>>
>>>
>>>
>>> def double_two(*num):
	lst2=[x*x for x in num]
	print(lst2)

	
>>> double_two(1,2,4)
[1, 4, 16]
>>>
>>>
>>>
>>>
>>> del list
>>> def double_two2(*num):
	lst2=map(lambda x: x*x,num)
	list(lst2)

	
>>> double_two2(1,2,4)
[1, 4, 16]
>>> def double_two2(*num):
	lst2=map(lambda x: x*x,num)
	return list(lst2)

>>> double_two(1,2,4)
[1, 4, 16]
>>> double_two2(1,2,4)
[1, 4, 16]
>>>
>>>
>>>
>>>
>>> def count(*num):
	from functools import reduce
	return reduce(lambda x,y:x+y,num)

>>> count(1,2,4)
7
>>>
>>>
>>>
>>>
>>> def double(*num):
	return [x*2 for x in num]

>>> double(1,2,4)
[2, 4, 8]
>>>
>>>
>>>
>>>
>>> lst1=[1,2,3]
>>> lst2=[4,5,6]
>>> list(zip(lst1,lst2))
[(1, 4), (2, 5), (3, 6)]
>>>
>>>
>>>
>>>
>>> def biggest(a,b,c):
	if a>b:
		maxnum=a
	else:
		maxnum=b
	if c>maxnum:
		maxnum=c
	return print(maxnum)

>>> biggest(1,2,3)
3
>>> biggest(4,6,9)
9
>>>
>>>
>>>
>>> def biggst2(*num):
	print(max(num))

	
>>> biggst2(1,2,3)
3
>>> 
