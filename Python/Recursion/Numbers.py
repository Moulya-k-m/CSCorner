def num(n):
    if (n==0):
        return 1
    else:
        num(n-1)
        print(n)

numb=num(5)
print(numb)