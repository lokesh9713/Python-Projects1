print('Number that are not divisible by 2 or 3 and lie in the range 1 to 50 are: ')
for i in range(1,51):
    if(i%2 != 0 and i%3 != 0):
        print(i)
