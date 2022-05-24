n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    arr1=list(map(int,input().strip().split()))
    arr2=list(map(int,input().strip().split()))
    k=arr1+arr2
    k.sort()
    print(*k)
  # print(len(k))