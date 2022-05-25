n=int(input())
for i in range(n):
    p='1234567890'
    k=input()
    c=0
    for j in k:
        if j in p:
            c=c+1
    if c==len(k):
        print("True")
    else:
        print("False")
#print(c,len(k))            
