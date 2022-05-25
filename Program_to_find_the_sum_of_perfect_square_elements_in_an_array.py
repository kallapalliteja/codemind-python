import math
def psqrt(n):
    k=int(math.sqrt(n))
    if k*k==n:
        return True
    else:
        return False
n=int(input())        
arr=list(map(int,input().strip().split()))
sum=0
for i in range(n):
    if psqrt(arr[i]):
        sum=sum+arr[i]
        #print(arr[i])
print(sum)        