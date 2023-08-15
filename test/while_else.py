####
i = 0
while i < 10:
    if i == 2:
        print(i)
        break   ## 循环到2就退出循环且不执行else下面的循环
    print(i)
    i+=1
else:
    print('结束')

a = 0
while a < 5:
    if a == 2:
        print('hello')
        a+=1
        continue   ## 退出当前一次循环继续下一次循环
    print('略')
    a+=1
else:
    print('结束')