#####python运算符
#### {(+加) (-减) (*乘) (/除) (//整除)  (%取余) (**幂指数) () 小括号} 
Num1 = 10
Num2 = 4
Num3 = 2
####加法 
print(f'{Num1 + Num2}')
####减法
print(f'{Num1 - Num2}')
#####乘法
print(f'{Num1 * Num2}')
#####除法
print(f'{Num1 / Num2}')
#####整除
print(f'{Num1 // Num2}')
######取余
print(f'{Num1 % Num2}')
#####幂指数
print(f'{Num1 ** Num2}')
#####优先级
print(f'{(Num1 + Num2) * Num3}')

#######求梯形面积 公式（上底+下底）×高÷2
Upperbottom = float(input('输入梯形上底'))
Bottom = float(input('输入梯形下底'))
high = float(input('输入梯形高'))
print(f'梯形面积为{(Upperbottom + Bottom) * high / 2}')

#####复合赋值将多个值赋值多个变量
A,B,C = 1,2,'hello,word'
print(A)
print(B)
print(C)
#####多个变量赋相同值
D = E = 6666
print(E)
print(D)
####复合赋值运算符
####（+=）(-=)(*=)(/=)(//=)(%=)(**=)
#####复合赋值运算符 计算顺序先执行算数在等于 例如：c+=a    等价于 c=c+a
Alan = 16
Jack = 2
Alan *= Jack
print(f'{Alan}')  ####输出为32


