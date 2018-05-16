year=int(input('请输入你想要计算的年分:'))
if year%4==0 and year%100==0:
    print('该年为润年:',year)
elif year%400:
    print('该年为平年:',year)
else:
    print('该年为平年:',year)
