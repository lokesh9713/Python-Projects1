print('Enter the sides of the triangle: ')
a = float(input('\tEnter a: '))
b = float(input('\tEnter b: '))
c = float(input('\tEnter c: '))
s = (a+b+c)/2;
area = (s*(s-a)*(s-b)*(s-c))**(0.5)
print('Area of triangle with sides a = {}, b = {} and c = {} is {}'.format(a,b,c,area))
