import math

n = 1000000

A = [True]*n

for a in range(0, n):
    A[a]=True

for i in range(2,int(round(math.sqrt(n)))):
    if A[i] == True:
        for j in range(pow(i,2), n, i):
            A[j] = False

for x in range(2,n):
    if A[x] == True:
        print x
