a=int(input())
c=0
for i in range(2,a):
    if a%i==0:
        print("not a prime")
        break
else:
    print("prime")
        