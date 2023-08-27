###函数嵌套
###函数嵌套就是在一个函数里面调用另外一个函数
def numA():
    print('这是函数A')


def numB():
    print('BBBBBBB')
    numA()

numB()