n=int(input())
arr=list(map(int,input().strip().split()))
for i in range(n):
    if arr.count(arr[i])>1:
        print(arr[i])
        break