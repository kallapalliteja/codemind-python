n=int(input())
p=n
rev=0
while(p):
    r=p%10
    p=p//10
    rev=rev*10+r
if(rev==n):
    print("True")
else:
    print("False")