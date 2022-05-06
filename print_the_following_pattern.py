n=int(input())
for i in range(n,0,-1):
    for j in range(1,n+2-i):
        print(j,end="")
    print()    