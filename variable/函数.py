####python 函数
'''
函数是一个被命名的、独立的、完成特定功能的代码段，其可能给调用它的程序一个返回值。

被命名的：在Python中，大部分函数都是有名函数
完成特定功能的代码段：函数的功能要专一，专门为了完成某个功能而定义
返回值：当函数执行完毕后，其可能会返回一个值给函数的调用处


函数的主要作用：
① 模块化编程
② 代码重用
'''
def greet(name):   
    print(f'hello,{name}')     

greet('alan') ###输出hello,alan
greet('jack')###输出hello,jack

'''
函数的设计原则“高内聚、低耦合”，
函数执行完毕后，应该主动把数返回给调用处，
而不应该都交由print()等函数直接输出。'''

def Username(Name):
    return 'hello-' + Name

print(Username('boby'))
print(Username('jacksk'))

def add_1(num):
    a = num + 1
    print(a)
    return num + 1

print(add_1(4),type(add_1(4))) ####5 <class 'int'>

'''Python函数的返回语句return严格意义上来说只能返回一个值，
可以是任何类型，
因此，可以通过返回一个“tuple元组”（定值表）类型值来间接达到返回多个值的目的'''
def res(x,y):
    a = x * y
    b = y -x
    return a,b
'''接收python返回的多个值时有两种方法，一种是建立变量进行接收，一种是操作字符串的方式进行接收，'''
###操作字符串方式
restue = res(4,5)

print(restue,type(restue)) ###(20, 1) <class 'tuple'

####建立变量方式
r1,r2 = res(7,8)
print(r1,r2,type(r1),type(r2)) ##56 1 <class 'int'> <class 'int'>

######函数嵌套
def testA():
    """函数注释"""
    print('AAA')
    print('AAAA')
def testB():
    """这里要调用函数A"""
    print('BBB')
    testA()  ###嵌套调用函数A
    print('上面调用函数A')
testB()



