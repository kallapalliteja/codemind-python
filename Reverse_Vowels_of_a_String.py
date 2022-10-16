n=input()
o='aeiouAEIOU'
p=""
for i in n:
    if i in o:
        p=p+i
z=p[::-1]
b=""
c=0
for i in n:
    if i in o:
        b=b+z[c]
        c=c+1
    else:
        b=b+i
print(b)        
        