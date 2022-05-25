n=input()
c=0
max=0
k='aeiouAEIOU'
for i in str(n):
    if i in k:
        c=c+1
    else:
        if c>max:
            max=c
            c=0
print(max)            
    