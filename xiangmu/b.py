def di(m):
    if m==1:
        return 1
    return m*di(m-1)
s = di(4)
print(s)
