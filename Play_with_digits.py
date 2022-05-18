n=int(input())
sum=0
arr=list(map(int,input().strip().split()))
z=[]
for i in range(n):
    p=arr[i]
    while(p):
        r=p%10
        p=p//10
        sum=sum+r
print(sum)
        