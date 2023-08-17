#####列表
name = ['alan','pute','jack','tiena','alan']
print (name[0])
print(name[1])
print(name[2])
####列表index
print(name.index('alan')) ###输出下标0
print(name.index('pute'))###输出下标1
###列表count，统计出现次数
print(name.count('alan')) ###输出2
### in 判断数据是否在列表里，如果在返回true否则返回false
print('alan'in name) ###true
print('blan'in name ) ###false
#### not in 判断数据不在某个列表，不在返回true，否则返回false
print('alan'not in name)  ###false
print('balan' not in name)  ###true
###append 追加
name.append('ck')
print(name)
###extend 列表结尾追加数据，如果是个数列，则按顺序加入
name.extend(['time','dave'])
print(name)
####insert 指定下标追加
name.insert(3,'tick')
print(name)
####删除列表del
del name[0]
print(name)
####pop()方法：删除指定下标的数据(默认为最后一个)，并返回该数据
name_list = name.pop(0)
print(name_list)
###remove()方法：移除列表中某个数据的第一个匹配项。
name.remove('dave')
print(name)
####clear()方法：清空列表，删除列表中的所有元素，返回空列表。
name.clear()
print(name)
###reverse()：将数据序列进行倒叙排列
Num = ['2','4','3','1','6','5']
Num.reverse()
print(Num)
###copy()方法：对列表序列进行拷贝
Num1 = Num.copy()
print(Num1)
####列表循环遍历while
i =0
while i < len(Num1):
    print(Num1[i])
    i+=1
####列表遍历for循环
for j in Num1:
    print(j)
####列表嵌套
Num2_list = [['alan','jack','tony'],['tick','boby','dave'],['time','flank','jojo']]
###查找flank，先查找存在的列表
print(Num2_list[2])
####在查找列表中的下标
print(Num2_list[2][1])


