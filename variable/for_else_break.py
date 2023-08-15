#### for else  break and contineu
str1 = 'hello'
for i in str1:
    if i == 'e':
     print('e不打印，循环结束')
     break
    print(i)
else:
    print('遇到break结束')
    
alse = 'ikbc'
for j in alse:
   if j == 'b':
    print('跳过b')
    continue
   print(j)
else:
   print('循环结束')
