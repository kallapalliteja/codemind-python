def evenodd(n):
    if n%2==0:
        return True
    else:
        return False
n=int(input())        
arr=list(map(int,input().strip().split()))
c=0
for i in range(n):
    l=len(str(arr[i]))
    #print(l)
    if(evenodd(l)):
        c=c+1
print(c)        
           
