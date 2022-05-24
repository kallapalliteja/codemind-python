n=int(input())
a=list(map(int,input().strip().split()))
b=list(map(int,input().strip().split()))
c=[]
i=0
for i in range(n):
    k=a[i]+b[i]
    c.append(k)
    i=i+1
print(*c)
