n=input()
k='0123456789'
c=0
for i in n:
    if i in k:
        c=c+1
if c==0:
    print("Doesn't contain digit")
else:
    print("Contains",c,"digit")