n = int(input('Enter the size of identity matrix (n): '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==j):
            print(' 1 ',end='')
        else:
            print(' 0 ',end='')
    print()
    