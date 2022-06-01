n1,n2=map(int,input().split())
arr1=set(map(int,input().strip().split()))
arr2=set(map(int,input().strip().split()))
c=list(arr1)+list(arr2)
p=[]
for i in range(len(c)):
    if i not in p and c.count(i)>1:
        p.append(i)
print(len(p))    
#print(arr1)
#print(arr2)