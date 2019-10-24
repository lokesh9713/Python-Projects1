print('Enter first number a : ',end='')
a = input();
print('Enter second number b : ',end='')
b = input();

#Using a THIRD VARIABLE
c = a
a = b
b = c
print('After swapping, a = {} and b = {}'.format(a,b))

