tc = float(input('Enter temperature in degree celcius: '))

# T(F) = T(C) * (9/5) + 32

tf = 9/5.0 * tc + 32
print('\n{} degree Celcius = {} degree Fahrenheit'.format(tc,tf))
