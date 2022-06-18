n=input()
k=[]
for i in n:
    k.append(n.count(i))
ma=max(k)
for i in n:
    if n.count(i)!=ma:
        print(i)
        break
else:
    print(-1)
    