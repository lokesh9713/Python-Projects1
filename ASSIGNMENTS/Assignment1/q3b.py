print('Enter first number a : ',end='')
a = float(input());
print('Enter second number b : ',end='')
b = float(input());

#Without using a THIRD VARIABLE
a = a + b
b = a - b
a = a - b
print('Again swapping, a = {} and b = {}'.format(a,b))
