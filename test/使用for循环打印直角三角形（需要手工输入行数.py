#使用for循环打印直角三角形（需要手工输入行数）
num = int(input('输入行数'))
for i in range(1,num+1):
    for j in range(i):
        print('*',end='\t')
    print('')

for a in range(1,10):
    print(a)
