####记口诀：切片其实很简单，只顾头来尾不管，步长为正正向移，步长为负则逆向移
Name = 'hello_world'
print(Name[1:3])
print(Name[4:]) ####输出o_world
print(Name[:4]) ####输出hell
print(Name[2::])###从第二位输出
print(Name[::4])###输出0-4-0-4 hor
print(Name[:-1])####祛除最后一位输出hello_worl
print(Name[::-1]) ####翻转字符串dlrow_olleh
print(Name[::-2])
print(Name[-4:-1])