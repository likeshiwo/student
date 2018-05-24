def jia(n):
    if n == 1:
        return 1
    return n*jia(n-1)
s = jia(4)
print(s)
