n=int(input())
for i in range(1,n+1):
    c=0
    a,b=map(int,input().split())
    for j in range(a,b+1):
        r=j%10
        if(r==2 or r==3 or r==9):
            c=c+1
    print(c)