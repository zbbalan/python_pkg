###python变量1
##变量是存储数据的容器
##在程序运行过程中可以发生改变
###变量存储的数据是临时的
##变量语法  变量名称 = 变量值
##变量由数字字母下划线组成，不能以数字开头，严格区分大小写
MyName = "zbb"
Date = 20230226
print(MyName,Date)
###数据类型分为{数值类型（init【整数型】，float【浮点型】）}{布尔型（真【True】，假【Flase】）}{字符串【str】}{list【列表】}{tuple【元组】}{set【集合】}{dict【字典print】}
###使用type返回变量类型
####使用isinstance返回变量是否使用正确
print(type(MyName))
print(type(Date))
print(isinstance(MyName,list))  ###MyName变量是str字符类所以返回false
print(isinstance(MyName,str)) ###MyName变量是str字符类所以返回true
####布尔值定义，变量值只有True和Flase两种 且首字母为大写
flage = True
print(type(flage))
print(isinstance(Date,bool)) ####可借助isinstance判断变量是否为真或假的布尔值进一步操作
#####数组类型和元组类型和set集合类型和dict字典类型
list_1 = [1,2,3,4,5,6,7] ###数组类型是可以在后续操作中改变值的__数组类型使用中括号表示
print(type(list_1)) ###输出为数组类型
tuple_1 = (8,9,10,11,12)####元组类型不可以在后续操作中改变值)_元组类型使用圆括号表示
print(type(tuple_1))####输出为tuple
set_1 = {2,4,6,8,10}#####set类型可以去重_使用花括号表示
print(type(set_1)) ####输出为set
dict_1 = {'A':'a','B':'b','C':'c'}####字典类型使用key：value键值对存在用于查询搜索
print(type(dict_1))#####输出为dict
##########python格式化输出%s_只能输出字符串
Name = 'hello'
YouNmae = 'word'
print("这是%s,这又是%s" % (Name,YouNmae))####类似于字符串传递变量
##########python格式化输出%d_只能输出整数型，%f输出浮点数 %.2f 小数点后保留两位
Title = 1
Price = 3.5
Today = "周日"
Category = "青菜"
ID = 2
print("今天是%s，%s%d斤%.2f元" % (Today,Category,Title,Price)) 
####%06d代表整数6位前面填充5个0
print("学号%06d" % (ID)) ####输出为000002
#####python3.6后简写格式化输出适用于字符串
#####formate
#####简写f{}
test = 'zbb'
mobile = '123456789'
print(f'姓名：{test},手机号：{mobile}') ####输出姓名：zbb,手机号：123456789
