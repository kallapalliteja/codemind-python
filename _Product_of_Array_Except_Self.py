n=int(input())
arr=list(map(int,input().strip().split()))
k=[]
for i in range(n):
    p=1
    for j in range(n):
        if i!=j:
            p=p*arr[j]
    print(p,end=" ")        
    
    
    
