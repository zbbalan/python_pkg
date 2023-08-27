####global关键字,在局部作用域中对全局作用域修改
num = 10
def func():
    global num ###使用global关键字在函数内修改全局变量
    num = 20
    print (num)


func()
