###判断用户输入的人名是否存在
name = ['alan','jack','bobe','dave']
name1 = input('输入查询人名')
if name1 in name:
    print(f'你要查的{name1},存在')
else:
    print(f'你要查的{name1},不存在')
