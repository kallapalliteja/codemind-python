n=int(input())
arr=list(map(int,input().strip().split()))
e=0
o=0
for i in range(n):
    if i%2==0:
        e=e+arr[i]
    else:
        o=o+arr[i]
if abs(e-o)==0:
    print("YES")
else:
    print("NO")