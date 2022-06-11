n=input()
for i in n:
    if ord(i)==46:
        print("[.]",end="")
    if ord(i)!=46:
        print(i,end="")
        