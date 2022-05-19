n=int(input())
arr=list(map(int,input().strip().split()))
k=[]
p=[]
m=(n-1)//2
for i in range(n):
    if i<=m:
        k.append(arr[i])
    else:
        p.append(arr[i])
    
for i in range(len(p)-1,-1,-1):
    print(p[i],end=" ")
for i in range(len(k)):
    print(k[i],end=" ") 
