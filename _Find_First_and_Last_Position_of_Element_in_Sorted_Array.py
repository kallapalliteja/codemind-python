n=int(input())
arr=list(map(int,input().strip().split()))
b=int(input())
for i in range(n):
    #print(arr[i])
    if arr[i]==b:
        print(i,end=" ")
        break
for j in range(n-1,-1,-1):
    if arr[j]==b:
        print(j,end=" ")
        break
if b not in arr:
    print(-1,-1)
    