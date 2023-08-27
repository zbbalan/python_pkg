def conde_num(num):
    '''' 方法主要生成指定长度的验证码，需要传递一个int类型的数值，return返回结果为numc长度的随机验证码
    '''
    import random
    ###定义一个随机字符串
    str = 'hdklkahdlkdjhaNK122J4141241JFLAJDFDKAHJKSLDHJahjkhjdlkadla'
    ###循环num次，代表生成num长度的字符串
    code = ''
    for i in range(num):
        index = random.randint(0,len(str)-1)
        code += str[index]
    return code

print(conde_num(10))