#常见数据类型
print("Hello")
print(type("Hello"))


print(type(10))
print(type(3.14))
print(type(True))
print(type(False))
print(type(None))

num=-100
print(type(num))
print(isinstance(num,int))



#字符串
#定义字符串的三种方式
s1 = "Hello" #双引号定义，不能换行
s2 = 'python' #单引号定义，不能换行
s3 = """
Hello:
    无论何时，我都喜欢初高中那个温柔的yyq
"""  #三引号定义多行字符串
print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))

#定义字符串---->It's a good time
#转义字符\' \" \n \t
msg='It\'s a good time'
print(msg)

print("\t无论何时，我都喜欢初高中那个温柔的yyq")

name="小卢"
age=18
str(age)
print(str(age),"我的名字叫"+name+"今年"+str(age)+"岁")

print(str(age),"我的名字叫%s今年%s岁"%(name,age))

print(str(age),f"我的名字叫{name}今年{age}岁")