num1 = 20 
num2 = 30

if num1 > num2 :
    print(f'最大值为{num1}')
else:
    print(f'最大值为{num2}')


####三目运算符简化

numN1 = 20
NUMN2 = 30

max = numN1 if numN1 > NUMN2 else NUMN2
print(f'最大值为{max}')