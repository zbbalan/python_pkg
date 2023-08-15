###求1-100偶数和
Num = 0
for i in range(101):
    if i %2 == 0:
        Num+=i
        print(f'所有偶数和{Num}')
####求1-100奇数和
Num1 = 0
for j in range(101):
    if j %2 != 0:
        Num1+=j
        print(f'所有奇数和{Num1}')