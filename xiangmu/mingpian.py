l=[]
import fozu
fozu.fozu()
def mingpian():
    print('*'*30)
    print('*'*30)

    print('欢迎使用[NCE名片管理系统]V1.0')
    while True:
        print('1.新建名片')
        print('2.显示全部')
        print('3.查询修改名片')
        print('4.删除名片')
        print('0.退出')

        print('*'*30)
        print('*'*30)
        ok=int(input('请输入想要操作的对应编号:'))
        if ok==1:
            diyi()
        elif ok==2:
            dider()
        elif ok==3:
            disan()
        elif ok==4:
            disi()
        elif ok==0:
            tuichu()
            break
        else:
            print('请不要乱输，谢谢!''\n')
def diyi():
    print('-'*30)
    print('-'*30)

    dic={}
    print('新建名片:')
    name=input('请输入您的姓名:')
    sex=input('请输入性别:')
    nian=input('请输入您的年龄:')
    gongsi=input('请输入您的公司:')
    python=input('请输入您的电话:')
    dizhi=input('请输入您的地址:')
    mail=input('请输入您的邮箱:')
    print('恭喜你新建完成!')
    dic={'姓名':name,'性别':sex,'年龄':nian,'公司':gongsi,'电话':python,'地址':dizhi,'邮箱':mail}
    l.append(dic)

    print('-'*30)
    print('-'*30)

def dider():
    print('>'*30)
    print('>'*30)
    print('显示全部名片')
    for dic in l:
        print('       公司:%s' % dic['公司'])
        print('姓名:%s''       电话:%s' % (dic['姓名'],dic['电话']))
        print('性别:%s''       地址:%s'     % (dic['性别'],dic['地址']))
        print('年龄:%s''       邮箱:%s'    % (dic['年龄'],dic['邮箱']))

    print('<'*30)
    print('<'*30)

def disan():
    print('&'*30)
    print('&'*30)
    print('查询名片')
    s=input('请输入姓名:')
    for dic in l:
        if s == dic['姓名']:
            print('       公司:%s' % dic['公司'])
            print('姓名:%s''       电话:%s' % (dic['姓名'],dic['电话']))
            print('性别:%s''       地址:%s'      % (dic['性别'],dic['地址']))
            print('年龄:%s''       邮箱:%s'     % (dic['年龄'],dic['邮箱']))
            you=input('请问你需要修改名片吗?(y/n)')
            if you == 'y':
                you1=input('请输入被修改人的名字:')
                if you1 == dic['姓名']:
                    newname=input('请输入你要修改的名字:')
                    dic['姓名']=newname
                    print('姓名:%s'% dic['姓名'])
                    print('修改成功!')
                elif you1 == dic['性别']:
                    newsex=input('请输入你要修改的性别:')
                    dic['性别']=newsex
                    print('性别:%s'% dic['性别'])
                    print('修改成功!')
                elif you1 == dic['年龄']:
                    newnian=input('请输入你要修改的年龄:')
                    dic['年龄']=newnian
                    print('年龄:%s'% nian['年龄'])
                    print('修改成功!')
                elif you1 == dic['电话']:
                    newdian=input('请输入你要修改的电话:')
                    dic['电话']=newdian
                    print('电话:%s'% newdian)
                    print('修改成功!')
                elif you1 == dic['地址']:
                    newdizhi=input('请输入你要修改的地址:')
                    dic['地址']=newdizhi
                    print('地址:%s'% dic['地址'])
                    print('修改成功!')
                elif you1 == dic['邮箱']:
                    newmail=input('请输入你要修改的邮箱:')
                    dic['邮箱']=newmail
                    print('邮箱:%s'% dic['邮箱'])
                    print('修改成功!')
                else:
                    print('操作有误，请细看操作说明!!')

        elif s != dic['姓名']:
            print('对不起，用户不存在!')

    print('&'*30)
    print('&'*30)
def disi():
    print('^'*30)
    print('^'*30)
    print('删除名片')
    shan=input('请输入你要删除名片的姓名:')
    for dic in l:
        if shan==dic['姓名']:
            l.remove(dic)
            print('删除成功!')
        else:
            print('用户不存在，无法删除!')

    print('^'*30)
    print('^'*30)
def tuichu():
    print('退出成功!')
mingpian()







