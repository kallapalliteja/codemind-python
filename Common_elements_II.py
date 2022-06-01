n1,n2=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
k=[]
for i in range(n1):
    if arr1[i] not in arr2:
        k.append(arr1[i])
for i in range(n2):
    if arr2[i] not in arr1:
        k.append(arr2[i])
print(*k)        