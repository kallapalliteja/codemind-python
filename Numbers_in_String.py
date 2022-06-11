n=input()
k='0123456789'
sum=0
for i in n:
    if i in k:
        sum=sum+int(i)
print(sum)        