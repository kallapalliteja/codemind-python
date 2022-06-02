n=int(input())
arr=list(map(int,input().split()))
c=0
min=999
for i in range(n):
    if len(str(arr[i]))<min:
        min=len(str(arr[i]))
for i in range(n):
    if len(str(arr[i]))==min:
        c=c+1
print(c)        
    