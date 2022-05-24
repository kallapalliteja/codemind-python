def prime(n):
    if n==0 or n==1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
n1=int(input())            
n2=int(input())
sum=n1+n2
i=1
while True:
   # sum=sum+i
    if prime(sum+i):
        print(i)
        break
    i=i+1
        
    
