n=int(input())
arr=list(map(int,input().strip().split()))
k=[]
sum=0
p=0
c=0
for i in range(n):
    if arr[i]!=-1:
        c=1
        for j in range(n):
            if arr[i]==arr[j] and i!=j:
                c=c+1
                arr[j]=-1
        if arr[i]==c:
            k.append(arr[i])
for i in range(len(k)):
    p=p+1
print(p)    
            
            
