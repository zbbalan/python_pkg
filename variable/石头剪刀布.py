##电脑随机出石头剪刀布，根据玩家出拳判断输赢平局
import random  ##导入随机数模块


player = int(input('请输入石头剪刀布,0--石头,1--剪刀,2--布'))
reboot = random.randint(0,2) ###随机0，2 之间
if player == reboot:
    print('平局')
elif (player == 0 and reboot == 1) or (player == 1 and reboot == 2) or (player == 2 and reboot == 0):
    print('你赢了')
else :
    print('你输了')