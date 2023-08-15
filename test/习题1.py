###用户猜随机（1~10之间的数字）只有三次机会，猜对打印yes，猜错打印error
import random
#user = int(input('输入数字'))
reboot = random.randint(1,10)
i = 0
while i < 3:
    user = int(input('输入数字'))
    if user == reboot: 
        print('yes')
        break
    elif user < reboot:
        print('猜小了')
    elif user > reboot:
        print('猜大了')
    i+=1 

