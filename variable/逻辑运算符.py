
####逻辑运算符 与或非
###  and 当表达式1为true 表达式2为true 则返回true ，若表达式1为true 表达式2为false则返回false 
##### or 当表达式1或表达式2其中一方为true是则返回true 除非表达式1与表达式2都为false时则返回false
#####   not 取反
Num1 = 5
Num2 = 6
Num3 = 11
print((Num1 > Num2) and (Num2 == Num1)) ###返回false
print((Num1 < Num2) and (Num1 < Num2))  ###返回true
print((Num1 < Num2) or (Num1 > Num2))   ###返回true
print((Num2 < Num1) or (Num2 > Num3))   ####返回false
print(not (Num1 > Num2) )  ####取反为true
