def prime(n):
    if n==0 or n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
n=int(input())
i=n
v=n
c1=0
c2=0
if prime(n):
    print(0)
else:
    
    while True:
        c1=c1+1
        if prime(i):
            z=i
            break
        i=i+1
    while True:
        c2=c2+1
        if prime(v):
            k=v
            break
        v=v-1
    if c1-1>c2-1:
        print(c2-1)
    else:
       print(c1-1)
    
    