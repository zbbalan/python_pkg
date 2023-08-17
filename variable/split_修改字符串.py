####split()修改字符串
mystr = 'Al,python,not,qucket,hello,and,to,Al'
print(mystr.split(',')) ###以逗号分割['Al', 'python', 'not', 'qucket', 'hello', 'and', 'to', 'Al']
print(mystr.split(',',1)) ###以第一个逗号分割，其余的不分割['Al', 'python,not,qucket,hello,and,to,Al']
print(mystr.split('*')) ###['Al,python,not,qucket,hello,and,to,Al']