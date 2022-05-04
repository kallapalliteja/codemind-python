import math
a=int(input())
for i in range(1,a+1):
    b=int(input())
    k=math.sqrt(b)
    p=int(k)
    if p*p==b:
        print("True")
    else:
        print("False")
    
    
