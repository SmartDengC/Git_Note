1：python包/模块的导入？  
	python导入的是一个 python package，如果是一个.py的单独文件，则无法导入  
2：import和 from..import...的区别？  
	import 是导入包中的所有模块，而 from..import...则是从包中导入某个模块。  
3：字典如何输出？  
	print(dicName[key])  

4：在进行设计对数据库增加和修改操作的时候，不知道怎么样做最好，现在只是将添加的信息硬塞在url里面，但是感觉数据不安全，其次就是url太长，不好操作。  
		开始的时候我是想传一个类对象，但是还没有实现这个。
		传一个json对象？  
5:如何将byte转换成dict？  
	从mqtt服务器接收到json格式的字符串是bytes类型的，要先转换成string，再用eval函数转换成字典。
	str1=str(msg.payload, encoding = "utf-8") ?
	data=eval(str1)
	print(data['name'])
	注意：str函数第二个参数encoding不能省略，不然出错。这几句在mqtt on_message里面调用  

6：web.input()与web.data()的差别？  
	web.input() 获取url参数，可以用于GET和POST请求包。  
	web.data() 获取实体正文，只能用用POST请求包。  
	
7：如何判断dict，tuple，list 值为空，某个key是否在其中？ 
```python 
	# 判断是否为空：
	if dict_name:
		print('不为空')
	# 判断是否有某个key：
	if ('key_name' in dict_name):
		pint('在其中')
```

8:测试代码？  

9：如何打开jupyter的notebook？  
	jupyter notebook  