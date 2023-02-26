#####input()输入______将输入作为变量赋值————————注意有input输入的变量都为字符串
Account = input('输入账户名称')
Password = input('输入密码')
print(type(Password))  ####输出为str
print(f'你输入的银行卡账户为{Account},密码为{Password}')
####案例将c1可乐变为牛奶 将c2牛奶变为可乐
c1 = input('输入c1变量')  ####在此输入可乐
c2 = input('输入c2变量')  #####在此输入牛奶
temp = c2
c2 = c1
c1 = temp
print(f'可乐为{c2},牛奶为{c1}')
#####day02的第三个视频