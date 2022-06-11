n=int(input())
for i in range(n):
    k=input()
    l=len(str(k))
    p=k
    rev=k[::-1]
    if p==rev and l%2==0:
        print("YES EVEN")
    elif p==rev and l%2!=0:
        print("YES ODD")
    else:
        print("NO")