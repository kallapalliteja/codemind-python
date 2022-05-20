n,a=map(int,input().split())
k=n%(10**a)
p=str(n)
m=p[::-1]
l=int(m)%(10**a)
z=str(l)
x=z[::-1]
print(abs(k-int(x)))
