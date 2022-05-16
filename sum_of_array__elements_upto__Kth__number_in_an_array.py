n=int(input())
arr=list(map(int,input().strip().split()))
k=int(input())
sum=0
for i in range(0,n):
    if arr[i]<=k:
        sum=sum+arr[i]
print(sum)        