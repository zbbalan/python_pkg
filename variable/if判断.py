#### if 判断
Num1 = 1
Num2 = 2

if True:
    print(Num1)   ####如果条件为true则输出num1的值

print("跳出if判断不受if影响----python判断受if的缩进来进行")



##案例1 年龄大于18岁输出可以上网
age = float(input('请输入你的年零：'))

if age >= 18:
    print(f'你的年龄为{age}，大于等于18岁可以上网')

####if else 判断  满足第一个条件输出 不满足进入else判断输出
###案例2 年龄大于18岁输出可以上网 不满足18岁输出年龄不够不让上网
if age >= 18:
    print(f'你的年龄为{age}，大于等于18岁可以上网')
else:
    print(f'你的年龄为{age}，小于18岁不可以上网')

###if elif else 多条件判断结构
"""如果条件1成立执行语句1 
如果条件2成立 执行语句段2 
都不成立执行语句else
"""
####案例根据工龄判断是否退休or上班or非法参数

Age1 = float(input("请输入你的年龄："))
if Age1 < 18 :
    print(f'你的年龄是{Age1},小于18，童工违法')
###elif Age1 > 18 and Age1 < 60 :
elif 18 <= Age1 <= 60 :     ####and 可以简写
    print (f'你的年龄是{Age1},大于18小于60，可上班')
###此段可简写elif 18 <= Age1 <= 60 :
###    print (f'你的年龄是{Age1},大于18小于60，可上班')
elif Age1 > 60 :
    print(f'你的年龄是{Age1},大于60,可以退休')
else:
    print('非法参数')

####day 2 第15个视频