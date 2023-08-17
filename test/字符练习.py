import random
###输入一个字符串，打印所有奇数位上的字符(下标是1，3，5，7…位上的字符)
a = input('输入字符串')
for i in range(0,len(a)):
   # print (i)
    if i % 2 ==1:
        print(a[i])
###输入用户名，判断用户名是否合法(用户名长度6~10位)
Name = len(input('输入用户名'))
if 6 <= Name <=10 :
    print('输入合法')
else:
    print('输入不合法')
###给定一个文件名，判断其尾部是否以".png"结尾
fileName = input("输入文件名称以.png结尾")
if fileName.endswith('png') == True :
    print('ok')
else:
    print('no')
#####给定一个字符串，如
'''mystr = "abcdefghijkopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
从字符串中随机取出4个字符，生成验证码
'''
mystr = "abcdefghijkopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
s=""
for a in range(4):
  mystr1 = random.randint(0,len(mystr))
  s+=mystr[mystr1]
print(s)
    






