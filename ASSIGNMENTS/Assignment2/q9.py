num = int(input('Enter a number: '))
n = 0
while(num>0):
    n += 1
    num //= 10
print('No. of digits in the number: ',n)