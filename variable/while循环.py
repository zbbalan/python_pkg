###对于循环次数已知的优先使用while循环
###初始化计数器
i = 0 
###编写循环条件
while i < 100 :
    print (f'{i+1}hello')
    ###更行计数器值
    i += 1


####案例 求和1....100的和
requse = 0
num = 1
while num <= 100:
    requse = num+requse
    print(requse)
    num+=1

####案例求1...100 中的偶数和
A = 1 
TestNum = 0
while A <=100:
    if A % 2 == 0:
        TestNum +=A
        
    A+=1
    print(TestNum)