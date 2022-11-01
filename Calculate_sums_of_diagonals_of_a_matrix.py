n=int(input())
a=[]
for i in range(n):
    l=list(map(int,input().split()))
    a.append(l)
pd=0
sd=0
for i in range(n):
    for j  in range(n):
        if i==j:
            pd=pd+a[i][j]
        if i==(n-1)-j:
            sd=sd+a[i][j] 
k1=str("Principal Diagonal:")+str(pd)  
k2=str("Secondary Diagonal:")+str(sd)
print(k1)
print(k2)
            