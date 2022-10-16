n=int(input())
for i in range(n):
    l=int(input())
    p=(str(l)[::-1])
    s=0
    k=0
    for i in p:
        s=s+(2**k)*int(i)
        k=k+1
    j=""
    while(s):
        r=s%8
        s=s//8
        j=j+str(r)
    print(j[::-1])    
    

    