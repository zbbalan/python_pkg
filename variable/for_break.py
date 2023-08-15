###for 循环中break和while中用法一致
Name = 'hello'
for i in Name:
    if i == 'e':
        print('退出循环')
        break
    print(i)