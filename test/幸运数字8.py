##幸运数字6（只要是6的倍数）：输入任意数字，如数字8，生成nums列表，元素值为1~8，从中选取幸运数字移动到新列表lucky，打印nums与lucky
import random
num1 = []
lucky = []
nums = int(input('输入数字'))
for i in range(1,nums+1):
    num1.append(i)
    for i in num1:
        if i %6 ==0:
            num1.remove(i)
            lucky.append(i)
print(num1)
print(lucky)

##有3个教室[[],[],[]]，8名讲师['A','B','C','D','E','F','G','H']，将8名讲师随机分配到3个教室中
teacher = ['a','b','c','d','e','f','g','h']
num3 = [[],[],[]]
for teachers in teacher:
    index = random.randint(0,2)
    num3[index].append(teachers)
i =1
for num3s in num3:
    print(f'第{i}教师老师是{num3s}')
    i+=1


