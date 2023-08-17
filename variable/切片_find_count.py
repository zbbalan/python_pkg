###find():检测某个字符串是否包含在这个字符串中，如果在返回下标，否则返回-1
mystr = 'my python not qucket hello and to git'
print(mystr.find('hello')) ####输出字符结束位置21，不写范围就在整个字符串中搜索
print(mystr.find('not',5,20)) ###在下标5到20之间搜索，下标结束位10
print(mystr.find('alan')) ###不存在显示-1
print(mystr.find('o'))
####rfind()和find功能相同，但查找从左边开始
###rindex()和rfind功能一样，都从左边查找
alan = 'hello.world'
print(alan.rfind('world'))
print(alan.rfind('hello'))
print(alan.rindex('world'))
print(alan.rindex('hello'))
###count(),返回某个字符在字符串的次数
mystar = 'my python not qucket hello and to git'
print(mystar.count('o')) ##输出4
print(mystar.count('and',1,30))