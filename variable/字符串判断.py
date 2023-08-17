#####startswith()检查字符串是否以指定字符串开头，是则返回true，否则返回false，如果设置开始结束位置下标，则在指定范围检查
#####endswitch（）检查字符串是否以指定字符串结束，是则返回true，否则返回false，如果设置开始结束位置下标，则在指定范围检查
mystr = 'hello python'
print(mystr.startswith('hello')) ### True
print(mystr.endswith('python'))   ###True
####isalpha()检测字符串是否有子母组成，是则true 否则false
mystr1 = 'hello1234'
mystr2 = 'hello'
print(mystr2.isalpha())  ###True
print(mystr1.isalpha())  ###false
###isdigit()：如果字符串只包含数字则返回 True 否则返回 False
mystr3 = '1234'
print(mystr1.isdigit())  ###false
print(mystr3.isdigit())  ###True