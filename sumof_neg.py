#kjsfdjask
n=int(input())
b=[]
for i in range(0,n):
    a=int(input())
    b.append(a)
s=0
t=0
u=0
for j in b:
    if(j>0):
        if(j%2==0):
            s=s+j
        else:
            t=t+j
    else:
        u=u+j
print(u)
