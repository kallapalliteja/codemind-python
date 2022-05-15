n=int(input())
arr=list(map(int,input().strip().split()))
sum=0
k=0
for i in range(n-1,-1,-1):
    sum=sum+(2**k)*arr[i]
    k=k+1
print(sum)    
    