'''
万事开头难，佛祖压阵前。
乱码一出现，怒气直冲天。
想要事事顺，佛祖来镇楼!
'''
#给大家开个玩笑哈!
import fozu
fozu.fozu()

#首先创建一个共同可用的列表
#列表
l=[]

#打包,还有千万别忘记缩进！！
def jinru():

#先做出几个大概的方向
    print('1.办理银行卡:')
    print('2.向卡内存钱:')
    print('3.查询卡内余额:')
    print('4.取出卡内余额:')
    print('5.积分兑换:')
    print('6.显示卡内信息')
    print('7.删除银行卡')
    print('0.退出:')
    print('')
    print('*'*50)
#然后完善这些需要填写的信息

#继续打包，以及缩进!!!
def banka():
    import time
    import random
    #随机一个银行卡号码
    ka=random.randint(100000000000000,999999999999999955)
    dic={}
    print('>'*50)
    print('')

    #完善第一步的信息
    print('你好，请准确完成以下操作!')
    print('')
    name=input('请输入您的姓名:')
    sex=input('请输入您的性别:')
    age=input('请输入您的年龄:')
    passwd=input('请输入您的六位数密码:')
    shouji=input('请输入您的手机号:')
    sfz=input('请输入您的身份证:')
    dizhi=input('请输入您的地址:')

    print('')
    print('-'*50)

    #要转换成浮点型!
    print('')
    money=float(input('请存放第一桶金:'))
    print('')
    print('请稍等...')
    time.sleep(0.5)
    print('请稍等...')
    time.sleep(0.5)
    print('请稍等...')
    print('')
    jifen=money*0.01
    print('你的银行卡号为:%d'% ka)
    print('')
    print('操作完成!请牢记您的银行卡密码')

    #输入完成之后就要全部装进>>字典里面
    dic={'姓名':name,'性别':sex,'年龄':age,'密码':passwd,'手机号':shouji,'身份证':sfz,'地址':dizhi,'账户余额':money,'银行卡':ka,'账户积分':jifen}

    #添加字典
    l.append(dic)
    print('')
    print('<'*50)

#查询
def cha():
    print('&'*50)
    print('')

    #接着完成第二项的查询
    print('欢迎使用查询余额功能!')
    print('')
    you_name=input('请输入您要查询用户的姓名:')
    you_passwd=input('请输入您要查询用户的密码:')
    print('')

    for dic in l:
        if you_name == dic['姓名']:
            if you_passwd == dic['密码']:
                print('-'*50)
                print('您的银行卡号是:',dic['银行卡'])
                print('')
                print('姓名:',dic['姓名'])
                print('账户余额:',dic['账户余额'])
                print('账户积分:',dic['账户积分'])
                print('')
                print('-'*50)
                break
            else:
                print('密码错误，请重输!')
    else:
        print('错误,账户不存在!')


#存钱内容的输出
def cun():
    print('^'*50)

    print('您好,欢迎使用存钱系统!')
    print('')
    name1=input('请输入姓名:')
    queren=input('请输入您的密码:')
    print('')
    for dic in l:
        if name1 == dic['姓名']:
            if queren == dic['密码']:
                print('')
                money=float(input('请输入存钱的金额:'))
                jifen=money*0.01
                print('')
                dic['账户余额']=dic['账户余额']+money
                dic['账户积分']=dic['账户积分']+jifen
                print('')
                print('你账户余额为:',dic['账户余额'])
                break
            else:
                print('密码错误，请重输!')
    else:
        print('错误,账户不存在!')
#存钱系统完毕

    print('^'*50)
#取钱内容的输出
def qu():
    print('-'*50)
    print('')
    print('您好,欢迎前来取钱!')
    print('')
    name1=input('请输入姓名:')
    queren=input('请输入您的密码:')
    print('')
    for dic in l:
        if name1 == dic['姓名']:
            if queren == dic['密码']:
                money=float(input('请输入取钱的金额:'))
                if dic['账户余额'] < money:
                    print('对不起，你没有这么多的钱!')
                    break
                dic['账户余额']=dic['账户余额']-money
                print('你账户余额为:',dic['账户余额'])
                break
                print('')
            else:
                print('密码错误，请重输!')
    else:
        print('错误,账户不存在!')
        print('-'*50)
#积分兑换的内容
def qiang():
    import time
    print('*'*50)
    print('欢迎使用积分兑换!')
    print('积分为你存入的金钱的:1%!')
    print('')
    name=input('请输入账户:')
    passwd=input('请输入密码:')
    for dic in l:
        if name == dic['姓名']:
            if passwd == dic['密码']:
                print('你现在的积分为:',dic['账户积分'])
                print('请输入序号，选择要对换的物品:')
                print('-'*50)
                print('')
                print('1.倚天剑:(200分)')
                print('2.屠龙刀:(250)')
                print('3.渣渣灰:(300)')
                print('4.葵花宝典:(500')
                print('5.佩琪亲手签名的衬衣!(700)')
                print('6.满宝石的无限手套:(1500)')
                print('0.算了')
                print('-'*50)
                #BUG 这里!!
                shuru=input('请选择:')
                if shuru == '1':

                    if dic['账户积分']<200:
                        print('对不起，你没有足够的积分!')
                    else:
                        dic['账户积分']=dic['账户积分']-200
                        time.sleep(0.5)
                        print('请稍等，礼物马上出现!')
                        time.sleep(0.5)
                        print('请稍等，礼物马上出现!')
                        time.sleep(0.5)
                        print('')
                        print('恭喜你获得倚天剑!')
                        print('积分剩余:',dic['账户积分'])

                elif shuru == '2':

                    if dic['账户积分']<250:
                        print('对不起，你没有足够的积分!')
                    else:
                        dic['账户积分']=dic['账户积分']-250
                        time.sleep(0.5)
                        print('请稍等，礼物马上出现!')
                        time.sleep(0.5)
                        print('请稍等，礼物马上出现!')
                        time.sleep(0.5)
                        print('')
                        print('恭喜你获得屠龙刀!')
                        print('积分剩余:',dic['账户积分'])

                elif shuru == '3':

                    if dic['账户积分']<300:
                        print('对不起,你没有足够的积分!')
                    else:
                        dic['账户积分']=dic['账户积分']-300
                        time.sleep(0.5)
                        print('请稍等，礼物马上出现!')
                        time.sleep(0.5)
                        print('请稍等，礼物马上出现!')
                        time.sleep(0.5)
                        print('')
                        print('恭喜你获得了渣渣灰!')
                        print('积分剩余:',dic['账户积分'])

                elif shuru == '4':

                    if dic['账户积分']<500:
                        print('对不起，你没有足够的积分!')
                    else:
                        time.sleep(0.5)
                        print('请稍等，礼物马上出现!')
                        time.sleep(0.5)
                        print('请稍等，礼物马上出现!')
                        time.sleep(0.5)
                        print('')
                        dic['账户积分']=dic['账户积分']-500
                        print('恭喜你获得葵花宝典!')
                        print('积分剩余:',dic['账户积分'])

                elif shuru == '5':

                    if dic['账户积分']<700:
                        print('对不起，你没有足够的积分!')
                    else:
                        time.sleep(0.5)
                        print('请稍等，礼物马上出现!')
                        time.sleep(0.5)
                        print('请稍等，礼物马上出现!')
                        time.sleep(0.5)
                        print('')
                        dic['账户积分']=dic['账户积分']-700
                        print('恭喜你获得了佩琪亲手签名的衬衣!')
                        print('积分剩余:',dic['账户积分'])

                elif shuru =='6':
                    if dic['账户积分']<1500:
                        print('对不起，你没有足够的积分!')
                    else:
                        time.sleep(0.5)
                        print('请稍等，礼物马上出现!')
                        time.sleep(0.5)
                        print('请稍等，礼物马上出现!')
                        time.sleep(0.5)
                        print('')
                        dic['账户积分']=dic['账户积分']-1500
                        print('恭喜你获得了满宝石的无限手套!(注意千万不要弹响指哦~)')
                        print('积分剩余:',dic['账户积分'])
                elif shuru == '0':
                    print('退出成功!')
                else:
                    print('您操作有误!')
                break
            else:
                print('密码错误，请重输!')
    else:
        print('错误，账户不存在!')
#卡内信息的输出
def liu():
    print('='*50)
    print('')

    print('欢迎使用查看功能!')
    name_new = input('请输入用户的姓名:')
    passwd_new = input('请输入密码:')
    for dic in l:
        if name_new == dic['姓名']:
            if passwd_new == dic['密码']:
                print('='*50)
                print('  你的银行卡号为:%d' % dic['银行卡'])
                print('        姓名:%s''      手机号:%s' % (dic['姓名'],dic['手机号']))
                print('        性别:%s''       地址:%s' % (dic['性别'],dic['地址']))
                print('        年龄:%s''       身份证:%s' % (dic['年龄'],dic['身份证']))
                print('  账户余额:%s''   账户积分:%s' % (dic['账户余额'],dic['账户积分']))
                print('='*50)
                break
            else:
                print('密码错误!请重输')
    else:
        print('账户不存在!')
def shanchu():
    print('^'*50)
    new_name=input('请输入你要删除的银行卡的账户:')
    passwd= input('请输入密码:')
    for dic in l:
        if new_name == dic['姓名']:
            if passwd == dic['密码']:
                l.remove(dic)
                print('删除成功!')
                break
            else:
                print('密码错误，无法删除!')
    else:
        print('账户不存在，无法删除!')
    print('^'*50)
def tuichu():
    print('退出成功!')

#接下来就是全部输出了,即将完事!
print('*'*50)
print('你好！欢迎来到只存不取银行!')

#这里要加上循环,不然只能操作一次!
while True:
    print('')
#开始进入项
    jinru()
    choose=int(input('请输入要操作系统的对应编号:'))
#办卡业务的输出
    if choose == 1:
        banka()
        print('')
#存钱业务的输出
    elif choose == 2:
        cun()
        print('')
#查询账户的输出
    elif choose == 3:
        cha()
        print('')
#取钱的操作输出
    elif choose == 4:
        qu()
        print('')
#积分兑换的输出
    elif choose == 5:
        qiang()
        continue
        print('')
#显示卡内信息的输出
    elif choose == 6:
        liu()
        continue
        print('')
#删除银行卡
    elif choose == 7:
        shanchu()
        print('')
#退出
    elif choose == 0:
        tuichu()
        break
    #方便自己检查:
    elif choose == 9:
        print(l)
    else:
        print('您好!你输入有误!')
