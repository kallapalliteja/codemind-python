n=int(input())
arr=list(map(int,input().strip().split()))
max=0
t=0
for i in range(n):
    c=1
    for j  in range(n):
        if arr[i]==arr[j] and i!=j:
            c=c+1
    if c==1:
        t=1
        if arr[i]>max:
            max=arr[i]
if t==0:
    print(-1)
else:
    print(max)