a=list(map(int,input().strip().split()))
b=list(map(int,input().strip().split()))
ai=0
bo=0
for i in range(3):
    if a[i]>b[i]:
        ai=ai+1
    elif a[i]<b[i]:
        bo=bo+1
print(ai,bo)        
    
        