###一些同学从1开始报数，当需要报出的数字尾数是7或者该数字是7的倍数时，则该同学跳过这个数字，不进行报数。所有同学都参与游戏后，游戏结束。如输入学生数量为50，游戏结束后，报数的同学数量为39。
##人数从0开始
num = int(input('输入数字'))
age = 0
for i in range(1,num+1) :
    if i % 7 == 0:
        continue
    if i % 10 == 7:
        continue
    age += 1
else:
    print(age)