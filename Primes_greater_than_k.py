def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())        
arr=list(map(int,input().strip().split()))
k=int(input())
c=0
for i in range(n):
    if arr[i]>=k and prime(arr[i]):
            c=c+1
print(c)            