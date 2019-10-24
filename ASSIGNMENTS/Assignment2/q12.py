from math import *
n = int(input('Enter a number: '))
for i in range(1,n+1):
    ls = []
    for j in range(1,i+1):
        ls.append(j)
    print(*ls,sep=' + ',end=' = ')
    print(fsum(ls))
    
