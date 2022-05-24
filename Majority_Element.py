n=int(input())
a=list(map(int,input().strip().split()))
max=0
for i in range(n):
    k=a.count(a[i])
    if k>max:
        max=k
        p=a[i]
print(p)        