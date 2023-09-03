###使用函数功能编写通讯录
''''
需求：进入系统显示系统功能界面，功能如下：
添加学员信息
删除学员信息
修改学员信息
查询学员信息
遍历所有学员信息
退出系统
系统共6个功能，用户根据自己需求选取

'''
''''
学员管理系统实现步骤
① 显示功能界面
② 用户输入功能序号
③ 根据用户输入的功能序号，执行不同的功能(函数)
定义函数
调用函数

'''

####封装menu函数打印功能页面
def menu():
    print('_'* 50)
    print('Alan_z 学生管理系统____v1.0')
    print('1.添加学员信息')
    print('2.删除学员信息')
    print('3.修改学员信息')
    print('4.查询学员信息')
    print('5.遍历所有学员信息')
    print('6.退出系统')
    print('_'* 50)

###所有功能使用前提是必须共享一套数据
###定义一个全局变量
info = []

####定义函数功能点一add_student 1.添加学员信息
def add_student():
    ####定义空字典接收name,age,mobile
    info_dict = {}
    info_dict['name'] = input('输入学员的姓名：')
    info_dict['age'] = input('输入学员的年领：')
    info_dict['mobile'] = input('输入学员联系方式：')
   ####修改全局变量，先声明全局变量
    global info
    info.append(info_dict)
    print('学员信息添加成功')
    print(info)


####定义函数功能点二，del_student，2.删除学员信息
def del_student():
    ####提示要删除的学员信息
    name = input('请输入要删除的学员信息')
    ###判断name是否存在info字典中
    for i in info:
        if i['name'] == name:
          ####查到学员工信息
            info.remove(i)
            print('学员信息删除成功')
            print(info)
            break
    else:
        print('未查询到要删除的学员信息')   

####定义函数功能3，modify_stduent,3.修改学员信息
def modify_student():
    name = input('请输入要修改的学员信息')
    global info
    ###判断name是否存在info字典中
    for i in info:
        if i['name'] == name:
            i['name'] = input('输入修改后学员的姓名：')
            i['age'] = input('输入修改后的年龄：')
            i['mobile'] = input('输入修改后的联系方式：')
            print('信息修改成功')
            break
    else:
        print('未查询到要修改的学员信息')

####定义函数功能4，find_student,4.查询学员信息
def find_student():
    name = input('请输入要查询的学员信息')
    for i in info:
        if i['name'] == name:
            print(f'学员姓名：{i["name"]},学员年龄：{i["age"]},学员的联系方式：{i["mobile"]},')
            break
    else:
        print('未查到要查到的学员信息')

###定义函数功能5 find_all ,5.遍历所有学员信息
def find_all():
    ####直接对info进行遍历操作
    for i in info:
        print(f'学员姓名：{i["name"]},学员年龄：{i["age"]},学员的联系方式：{i["mobile"]},')

####使用死循环让程序一直执行
while True:
    menu()

####使用input接受用户输入信息
    user_num = int (input('输入你要执行的序号：'))
    ####使用if多分枝条件实现不同的功能
    if user_num == 1:
        ####添加学员信息
        add_student()
    elif user_num == 2:
        ####删除学员信息
        del_student()
    elif user_num == 3:
        ###修改学员信息
        modify_student()
    elif user_num == 4:
        ###查询学员信息
        find_student()
    elif user_num == 5:
        ###遍历所有学员信息
        find_all()
    elif user_num == 6:
        ###退出系统
        print('感谢使用')
        break
    else:
        print('信息输入错误')
