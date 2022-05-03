'''import math
a=int(input())
c=math.log10(a)+1
while a:
    r=a%10
    a=a/10
    if r%2==0:
        e+=1
        mix+=1
    else:
        od+=2
        mix-=1
if c==e:
    print("Even")
    if 2*c==od:
        print("Odd")
    else:
            print("Mixed")'''
n=int(input()) #546 
c=0
s=0
for i in str(n): #"546"
    if(int(i)%2==0): #
        c+=1
    elif(int(i)%2!=0):
        s+=1
if(c==len(str(n))):
    print("Even")
elif(s==len(str(n))):
    print("Odd")
else:
    print("Mixed")
        