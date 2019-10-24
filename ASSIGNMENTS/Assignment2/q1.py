list1 = []
num = int(input('Enter the number of values in the list: '))
print('\nEnter the values of list: ')
for i in range(1,num+1):
    val = float(input())
    list1.append(val)
sum = 0
for val in list1:
    sum += val
print('Average of numbers in the list {} is: {}'.format(list1,sum/len(list1)))
    