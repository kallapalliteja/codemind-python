n=input()
x=0
y=0
for i in str(n):
    if i=='z':
        x=x+1
    else:
        y=y+1
if 2*x==y:
    print("Yes")
else:
    print("No")