L=int(input())
n=int(input())
for i in range(1,n+1):
    w,h=map(int,input().split())
    if(w<L or h<L):
        print("UPLOAD ANOTHER")
    elif(w==h):
        print("ACCEPTED")
    else:
        print("CROP IT")
        