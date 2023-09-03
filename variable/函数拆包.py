###python中拆包，就是把元组或者字典数据单独拆出，然后赋予变量



def num ():
    return 100,200  ##返回的是元祖类型

cluster_num,cluster_num2 = num() ####变量把元组中每个数据拆包
print(cluster_num)  ###100
print(cluster_num2) ###200



dict1 = {'name':'jack','age':'18'} ####字典拆包，只能把每个元素的key拆出来
a,b = dict1
print(a) ####name
print(b) ####age
###获取字典中的数据
print(dict1[a]) ###jack
print(dict1[b]) ###18