n=int(input())
arr=list(map(int,input().strip().split()))
b=int(input())
c=0
for i in range(n):
    if arr[i]==b:
        print(arr.index(b))
        c=c+1
if c==0:
    print(-1)