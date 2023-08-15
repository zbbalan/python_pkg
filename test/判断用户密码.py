'''用for循环实现用户登录
① 输入用户名和密码
② 判断用户名和密码是否正确（username='admin'，password='admin888'） 
③ 登录仅有三次机会，超过3次会报错 

分析：用户登陆情况有3种:
① 用户名错误(此时便无需判断密码是否正确)  -- 登陆失败 
② 用户名正确 密码错误 --登陆失败 
③ 用户名正确 密码正确 --登陆成功
'''
num = 0
for i in range(3) :
    Uname = input('输入用户名')
    Pword = input('输入密码')
    num +=1 ####更新计数器，下面使用if嵌套
    if Uname == 'admin':
        if Pword == 'admin888':
            print('登录成功')
            break
        else:
            print('密码错误')
            print(f'还有{3-num}次机会')
    else:
        print('用户名错误')
        print(f'还有{3-num}次机会')
    




