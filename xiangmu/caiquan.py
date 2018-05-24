def caiquan():
    import random
    pc=random.randint(1,3)
    print('我们来玩个猜拳游戏把')
    a='石头'
    b='剪刀'
    c='布'
    user=input('请输入石头/剪刀/布:')
    if user=='石头':
        print('你出了:石头')
    elif user=='剪刀':
        print('你出了:剪刀')
    elif user =='布':
        print('你出了:布')
    else:
        print('输入有误')
    if pc==1:
        print('斯塔克出了:石头')
    elif pc==2:
        print('斯塔克出了:剪刀')
    else:
        print('斯塔克出了:布')
    if (user=='石头' and pc==2) or (user=='剪刀' and pc==3) or (user=='布' and pc==1):
        print('你赢了')
    elif  (user=='石头' and pc==3) or (user=='剪刀' and pc==1) or (user=='布' and pc==2):
        print('你输了')
    elif pc == user:
        print('平局')
    else:
        print('操作有误,无法继续!')
