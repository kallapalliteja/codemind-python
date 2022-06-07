n=int(input())
a=list(map(int,input().split()))
c=0
max=0
for i in range(n):
    if a[i]!=0:
        c=c+1
    elif a[i]==0:
        c=0
    if c>max:
        max=c
print(max)        
    