hd = 4
for i in range(0,hd):
    for j in range(0,hd-i-1):
        print(end = ' ')
    for k in range(0,i+1):
        print('/',end = '')
    for l in range(0,i+1):
        print('\\',end = '')
    print()
for i in range(0,hd):
    for j in range(0,i):
        print(end = ' ')
    for k in range(0,hd-i):
        print('\\',end = '')
    for l in range(0,hd-i):
        print('/',end = '')
    print()