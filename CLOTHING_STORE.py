n=int(input())
arr=list(map(int,input().strip().split()))
t=0
for  i in range(n):
    c=1
    if(arr[i]!=-1):
    
        for j in range(n):
            if arr[i]==arr[j] and i!=j:
                c=c+1
                arr[j]=-1
        if c>=1:
            t=t+c//2
print(t)        
