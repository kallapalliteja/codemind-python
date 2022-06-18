n1=input()
n2=input()
k=n1+n2
p=[]
for i in k:
    p.append(i)
p.sort()    
s=''
for i in range(len(p)):
    s=s+p[i]
print(s)    