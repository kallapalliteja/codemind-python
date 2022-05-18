n=int(input())
arr=list(map(int,input().strip().split())) # 1 2 3 4 5 6 7
a,b=map(int,input().split())
sum=0# 0 1 2 3 4 5 6
for i in range(n):
    if arr[i]>=a and arr[i]<=b:
        sum=sum+arr[i]
print(sum)        
