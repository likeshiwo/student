che=input('请选择你要乘坐的车(城市公共汽车/轨道交通):')
if che=='城市公共汽车':
    print('城市公共电汽车价格调整为：10公里(含)内2元，10公里以上部分，每增加1元可乘坐5公里。使用市政交通一卡通刷卡乘坐城市公共电汽车，市域内路段给予普通卡5折，学生卡2.5折优惠;市域外路段维持现行折扣优惠不变。享受公交政策的郊区客运价格，由各区、县政府按照城市公共电汽车价格制定。')
    potong=input('请选择你要刷的卡(普通卡，学生卡，无卡):')
    if potong==('普通卡'):
        ka=int(input('请你输入的距离:'))
        if ka>10:
            money=(2+(ka-10)/5*1*0.5)*30
            a=float(money)
            if a>money:
                a=a+1
                print('你本月所需要支付:',a,'元')
            else:
                print('你本月需要支付:',a,'元')
        else:
            money=2*0.5*30
            a=float(money)
            if a>money:
                a=a+1
                print('你本月所需要支付:',a,'元')
            else:
                print('你本月需要支付:',a,'元')
    elif potong==('学生卡'):
        ka=int(input('请你输入的距离:'))
        if ka>10:
            money=(2+(ka-10)/5*1*0.25)*30
            a=float(money)
            if a>money:
                a=a+1
                print('你本月所需要支付:',a,'元')
            else:
                print('你本月需要支付:',a,'元')
        else:
            money=2*0.25*30
            a=float(money)
            if a>money:
                a=a+1
                print('你本月所需要支付:',a,'元')
            else:
                print('你本月需要支付:',a,'元')
    else:
        ka=int(input('请你输入距离:'))
        if ka>10:
            money=(2+(ka-10)/5*1)*30
            a=float(money)
            if a>money:
                a=a+1
                print('你本月所需要支付:',a,'元')
            else:
                print('你本月需要支付:',a,'元')
        else:
            print('你本月需要支付:60元')
elif che=='轨道交通':
    print('轨道交通价格调整为：6公里(含)内3元;6公里至12公里(含)4元;12公里至22公里(含)5元;22公里至32公里(含)6元;32公里以上部分，每增加1元可乘坐20公里。使用市政交通一卡通刷卡乘坐轨道交通，每自然月内每张卡支出累计满100元以后的乘次，价格给予8折优惠;满150元以后的乘次，价格给予5折优惠;支出累计达到400元以后的乘次，不再享受打折优惠。')
    ka=input('请刷卡(一卡通，无卡)')
    if ka=='无卡':
        juli=int(input('请输入距离:'))
        if juli<=6:
            print('你本月需要支付:90元')
        elif juli>=6 and juli<=12:
            print('你本月需要支付:210元')
        elif juli>=12 and juli<=22:
            print('你本月需要支付:360元')
        elif juli>=22 and juli<=32:
            print('你本月需要支付:540元')
        else:
            moeny=(18+(juli-32)/20*1)*30
            a=float(money)
            if a>money:
                a=a+1
                print('你本月所需要支付:',a,'元')
            else:
                print('你本月需要支付:',a,'元')
    if ka=='一卡通':
        juli=int(input('请输入距离:'))
        if juli<=6:
            print('你需要支付:90元')
        elif juli>=6 and juli<=12:
            money=7*30*0.5
            a=float(moeny)
            if a>money:
                a=a+1
                print('你本月所需要支付:',a,'元')
            else:
                print('你本月需要支付:',a,'元')
        elif juli>=12 and juli<=22:
            money=12*30*0.5
            a=float(money)
            if a>money:
                a=a+1
                print('你本月所需要支付:',a,'元')
            else:
                print('你本月需要支付:',a,'元')
        elif juli>=22 and juli<=32:
            money=(18*30-400)+400*0.5
            a=float(money)
            if a>money:
                a=a+1
                print('你本月所需要支付:',a,'元')
            else:
                print('你本月需要支付:',a,'元')
        else:
            money=(18+(juli-32)/20*1)*30
            a=float(money)
            if a>=400:
                money1=400*0.5+(a-400)
                b=float(money1)
                if b>money1:
                    b=b+1
                    print('你本月所需要支付:',b,'元')
                else:
                    print('你本月需要支付:',b,'元')
            else:
                money2=(18+(juli-32)/20*1)*30*0.5
                b=float(money2)
                if b>money2:
                    b=b+1
                    print('你本月所需要支付:',b,'元')
                else:
                    print('你本月需要支付:',b,'元')
