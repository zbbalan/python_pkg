###for 循环中contonue使用方式和while中一样
name = 'hello'
for i in name:
    if i == 'l':
        print('跳过')
        continue
    print(i)