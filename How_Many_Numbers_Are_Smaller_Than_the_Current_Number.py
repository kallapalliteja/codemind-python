n=int(input())
arr=list(map(int,input().strip().split()))
for i in range(n):
    c=0
    for j in range(n):
        if arr[i]>arr[j]:
            c=c+1
    print(c,end=" ")        