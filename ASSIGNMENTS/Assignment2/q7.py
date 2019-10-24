print('Enter three digits: ')
a = int(input('\tFirst: '))
while(a<0 or a>9):
    print('WRONG INPUT !!!! ENTER AGAIN...')
    a = int(input('\tFirst: '))
b = int(input('\tSecond: '))
while(b<0 or b>9):
    print('WRONG INPUT !!!! ENTER AGAIN...')
    b = int(input('\tSecond: '))
c = int(input('\tThird: '))
while(c<0 or c>9):
    print('WRONG INPUT !!!! ENTER AGAIN...')
    a = int(input('\tThird: '))
list1 = []
perm = []
list1.append(a)
list1.append(b)
list1.append(c)
for i in range(0,len(list1)):
    for j in range(0,len(list1)):
        for k in range(0,len(list1)):
            if(i!=j and j!=k and i!=k):
                perm.append((list1[i],list1[j],list1[k]))
            k += 1
        j += 1
    i += 1
perm_set = set(perm)
print(perm_set)
