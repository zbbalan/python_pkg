####字符串修改 replace (旧字符串，新字符串，替换次数)
mystr = 'Al python not qucket hello and to Al'
print(mystr.replace('and','&'))
print(mystr.replace('Al','BL',2))
print(mystr)#####注意：数据按照是否能直接修改分为可变类型和不可变类型两种。由于字符串属于不可变类型，所以修改的时候不能改变原有字符串