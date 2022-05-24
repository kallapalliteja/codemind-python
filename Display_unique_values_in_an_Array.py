n=int(input())
a=list(map(int,input().strip().split()))
c=0
for i in range(n):
    if a.count(a[i])==1:
        c=c+1
        print(a[i],end=" ")
if c==0:
    print(-1)