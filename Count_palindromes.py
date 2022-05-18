def rev(n):
    p=n
    k=0
    while(n):
        r=n%10
        n=n//10
        k=k*10+r
    if p==k:
        return True
    else:
        return False
        
n=int(input())
arr=list(map(int,input().strip().split()))
c=0
for i in range(n):
    if rev(arr[i]):
        c=c+1
print(c)        
        
