####for 循环
'''Python2 range() 函数返回的是列表，
而在Python3中 range() 函数返回的是一个可迭代对象（类型是对象），而不是列表类型， 
所以打印的时候不会打印列表。'''
Num = int(5)
for i in range (Num):
    print(i)
Name = 'hello'
for j in Name:
    print (j)