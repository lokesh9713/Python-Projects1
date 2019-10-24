print('Enter the lower and upper range limit: ')
low = int(input('\tLower limit: '))
up = int(input('\tUpper Limit: '))
while(up<=low):
    print('WRONG INPUT... ENTER AGAIN....')
    up = int(input('\tUpper Limit: '))
num = int(input('Enter the number to be divided by: '))
print('Numbers in the range [{},{}] divisible by {} are : '.format(low,up,num))
for i in range(low,up+1):
    if(i % num == 0):
        print(i)
