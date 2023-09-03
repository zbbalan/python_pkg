####函数中数据传递
def func (*args,**kwargs):
    print(args)
    print(kwargs)

###先定义一个元组
tuple1 = (10,20,30,40)
####再定义一个字典
tuple2 = {'age':18,'send':28}
#####需求如下：把元组传递给args，把字典传递给kwargs
####如果想把元组传递给args要在调用函数的tuple1 前面加一个*号
####如果想把字典传递给tuple2 要在调用函数tuple2前面加2个*号
func(*tuple1,**tuple2)