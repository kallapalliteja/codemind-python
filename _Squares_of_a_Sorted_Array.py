n=int(input())
arr=list(map(int,input().strip().split()))
k=[]
for i in range(n):
    p=abs(arr[i])
    k.append(p**2)
k.sort()
print(*k)