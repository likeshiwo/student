b=0
for a in range(101,201):
    k=0
    for i in range(2,a):
        if a%i==0:
            k=k+1
    if k==0:
        print(a)
        b=b+1
print('素数一共有',b,'个')
