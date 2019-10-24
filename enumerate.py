def prime_ones(li):
    for i,x in enumerate(li):
        if (x is not 0 and x is not 1):
            flag = 0
            for j in range(2,x//2 + 1):
                if(x % j == 0):
                    flag = 1
                    break
            if(flag == 0):
                li[i] = x/x
        
li = list(range(0,21))
prime_ones(li)
print(li)

square_odd = [n**2 for n in range(0,10) if n%2!=0]
print(square_odd)
                
dateStr = '13-11-1997'
day,month,year = dateStr.split('-')

'/'.join([month,day,year])

planet = 'Pluto'
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(planet, pluto_mass, pluto_mass / earth_mass, population))