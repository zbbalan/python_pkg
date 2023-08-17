#####元组特点：定义元组使用小括号，且使用逗号隔开各个数据，数据可以是不同的数据类型。
#####注意：如果定义的元组只有一个数据，那么这个数据后面也要添加逗号，否则数据类型为唯一的这个数据的数据类型。
num1 = (10,20,30)
num2 = (40,)
num3 = (50)
print(type(num1)) ###<class 'tuple'>
print(type(num2)) ####<class 'tuple'>
print(type(num3)) ###<class 'int'> 
####元组内的数据如果直接修改则立即报错，但是如果元组里面有列表，修改列表里面的数据则是支持的，故这个特点非常重要。
tuple = (10,20,['AA','bb'],31,33)
print(tuple[2])
tuple[2][0]='aa'
print(tuple)
####元组相关操作
tuple1 = ('aa','bb','cc','dd','dd')
print(tuple1[1])###bb
print(tuple1.index('cc')) ###2
print(tuple1.count('dd')) ###2
print(len(tuple1)) ###5


