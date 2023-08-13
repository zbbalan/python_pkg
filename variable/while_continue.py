####continue 关键字，跳出这次循环，继续下个循环
i= 1 
while i <= 10:
    if i == 4:
        i += 1 ##### 使用continue必须在更新计数器
        print('这步跳过')
        continue
    print(f'这是{i}')
    i+=1
    
