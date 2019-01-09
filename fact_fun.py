#jidskjflsk
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
s,k=input().split()
s=int(s)
k=int(k)
d=factorial(s)//factorial(k)
print(d)
