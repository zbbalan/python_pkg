####比较运算符只返回布尔值
####==绝对等于 != 不等于 >大于 <小于 >= 大于等于 <=小于等于
Num1 = 2
Num2 = 3
Num3 = 5
print(Num1 > Num2) ###输出结果为False
print(Num2 > Num1)  ####输出结果未True
print((Num1 + Num2)==Num3) ####输出结果未True

###求园的半径
##公式 S= 3.14 *2
r = float(input('请输入圆的半径'))
PI = 3.14
S = PI * r ** 2
print (f'圆的半径为：{S}')


###计算BIM值
##公式BIM=体重/身高的平方
Sg = float(input('请输入身高：'))
TG = float(input('请输入体重：'))
BIM = TG / Sg ** 2
print(f'BIM值为{BIM}')
