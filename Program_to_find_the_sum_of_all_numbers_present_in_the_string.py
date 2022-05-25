n=input()
k='123456789'
sum=0
for i in str(n):
    if i in k:
        sum=sum+int(i)
print(sum)        