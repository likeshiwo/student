def mingpian():
    print('*'*30)

    print('欢迎使用[NCE名片管理系统]V1.0')
    while True:
        print('1.新建名片')
        print('2.显示全部')
        print('3.查询名片')
        print('4.删除名片')
        print('0.退出')

        print('*'*30)
        ok=int(input('请输入:'))
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

    dic={}
    print('请按要求完成以下内容:')
    name=input('请输入您的姓名:')
    sex=input('请输入性别:')
    qq=input('请输入您的QQ:')
    mail=input('请输入您的邮箱:')
    python=input('请输入您的电话:')
    dizhi=input('请输入您的地址:')
    print('恭喜你新建完成!')
    dic['姓名']=name
    dic['性别']=sex
    dic['QQ']=qq
    dic['邮箱']=mail
    dic['电话']=python
    dic['地址']=dizhi
    print('-'*30)

def dider():
    print('显示全部名片')
    print(dic)

def disan():
    print('查询名片')
def disi():
    print('删除名片')
def tuichu():
    print('退出成功!')
mingpian()







