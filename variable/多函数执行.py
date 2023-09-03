num = 0
def test1():
    global num
    num = 100
   # print(num)

def test2():
    print(num)

test1() ####必须先执行test1函数后test2()函数才能生效
test2() ####100



##把函数返回值作为参数传递
def Num():
    return 1001
def Num2(Nnum):
    print(Nnum)

result = Num()  ###保存函数Num（）的值
Num2(result)###将返回值所在的变量作为参数传递到Num2函数




###函数调用，通过“键=值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。
####函数调用时，如果有位置参数时，位置参数必须在关键字参数的前面，但关键字参数之间不存在先后顺序
def user_info(name,age,gender):
    print(f'你的名字是{name},年龄{age},性别{gender}')

user_info(name='jack',age='20',gender='男')
user_info('Ana',age=18,gender='女')
user_info('tina',gender='女',age=19)

####缺省函数传参
####缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值（注意：所有位置参数必须出现在默认参数前，包括函数定义和调用）。

def gender_info(Name,Age,Gender='男'):
    print(f'你的名字{Name},你的年龄{Age},你的性别{Gender}')

gender_info('Jack',18,)
gender_info('rose',20,'女')  ###函数调用时，如果为缺省参数传值则修改默认参数值；否则使用这个默认值。

####包裹位置传递参数
###不定长参数也叫可变参数。用于不确定调用的时候会传递多少个参数(不传参也可以)的场景。此时，可用包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便
def verb_info(*args): ##返回是元组类型参数
    print(args)

verb_info('Tom')
verb_info('jaske',18,'女')

####包裹关键字传递
####无论是包裹位置传递还是包裹关键字传递，都是一个组包的过程。

def wan_info(**kwargs):  ###返回是字典类型的参数
    print(kwargs)

wan_info(NAme='boby',args=22,genders='男')