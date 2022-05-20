import math
n=int(input())
for i in range(n):
    if i**2==n:
        print("True")
        break
else:
    print("False")