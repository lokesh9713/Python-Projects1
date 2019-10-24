n = int(input('Enter the number of rows: '))
print()
for i in range(0,n):
    for j in range(0,i+1):
        print(end='  ')
    for j in range(2*(n-i)-1,0,-2):
        print(' *  ',end='')
    print()
   