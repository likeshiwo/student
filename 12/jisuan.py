def jia(a,b):
    return a+b
def jian(a,b):
    return a-b
def cheng(a,b):
    return a*b
def chu(a,b):
    return a/b
print('欢迎使用斯塔克计算机!')
row='p'
while row!='q':
    l=input('如果不想使用请输入q,使用输入ok进行下一步:')
    if l=='q':
        row='q'
        break
    elif l=='ok':
        x=int(input('请输入第一位数:'))
        fuhao=input('请输入+ - * /:')
        y=int(input('请输入第二位:'))
        if fuhao=='+':
            s=jia(x,y)
            print('答案是:',s)
            y1=int(input('请输入第三位:'))
            qw=s+y1
            print('答案是:',qw)
        elif fuhao=='-':
            d=jian(x,y)
            print('答案是：',d)
            y2=int(input('请输入第三位:'))
            qw1=d-y2
            print('答案是:',qw1)
        elif fuhao=='*':
            f=cheng(x,y)
            print('答案是：',f)
            y3=int(input('请输入第三位:'))
            qw2=f*y3
            print('答案是:',qw2)
        elif fuhao=='/':
            g=chu(x,y)
            print('答案是：',g)
            y4=int(input('请输入第三位:'))
            qw3=g/y4
            print('答案是:',qw3)
        else:
            print('别乱输，否则我锤死你!')
    else:
        print('在乱输,我锤死你!')
        break
