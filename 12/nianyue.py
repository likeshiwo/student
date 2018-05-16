year=int(input('请输入年:'))
year1=int(input('请输入月:'))
year2=float(input('请输入日:'))
if year%4==0 and year%100!=0 or year%400==0:
    if year1==1:
        a=year
        year1=0
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==2:
        a=year
        year1=31
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==3:
        a=year
        year1=29+31
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif yea1==4:
        a=year
        year1=29+31+31
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==5:
        a=year
        year1=29+31+31+30
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==6:
        a=year
        year1=29+31+31+30+31
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==7:
        a=year
        year1=29+31+31+30+31+30
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==8:
        a=year
        year1=29+31+31+30+31+30+31
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==9:
        a=year
        year1=29+31+31+30+31+31+31+30
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==10:
        a=year
        year1=29+31+31+30+31+31+31+30+30
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==11:
        a=year
        year1=29+31+31+30+31+31+31+30+30+31
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==12:
        a=year
        year1=29+31+31+30+31+31+31+30+30+31+30
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    else:
        print('别乱输，我很累的!')
else:
    if year1==1:
        a=year
        year1=0
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==2:
        a=year
        year1=31
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==3:
        a=year
        year1=28+31
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==4:
        a=year
        year1=28+31+31
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==5:
        a=year
        year1=28+31+31+30
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==6:
        a=year
        year1=28+31+31+30+31
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==7:
        a=year
        year1=28+31+31+30+31+30
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==8:
        a=year
        year1=28+31+31+30+31+30+31
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==9:
        a=year
        year1=28+31+31+30+31+31+31+30
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==10:
        a=year
        year1=28+31+31+30+31+31+31+30+30
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==11:
        a=year
        year1=28+31+31+30+31+31+31+30+30+31
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    elif year1==12:
        a=year
        year1=28+31+31+30+31+31+31+30+30+31+30
        b=float(year1)
        c=year2+b
        print('是',a,'年的第',c,'天')
    else:
        print('别乱输,我很累的!')

