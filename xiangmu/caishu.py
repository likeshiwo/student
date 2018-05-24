def caishu():
    import random
    print('测测你能不能读懂我的心')
    n=random.randint(1,100)
    while True:
        num=int(input('输入你认为的数字 1-100:'))
        if num<n:
            print('你猜的数太小啦')
        elif num > n:
            print('你猜的数太大啦')
        else:
            print('漂亮！恭喜你猜对了(虽然没什么用)！')
            break

