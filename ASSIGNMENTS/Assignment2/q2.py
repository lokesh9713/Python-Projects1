num = int(input('Enter a number: '))

list1=[]
while(num>0):
    rem = num % 10
    list1.append(rem)
    num //= 10
n = len(list1)-1
rev = 0
for val in list1:
     rev += val*(10**n)
     n = n-1
print('Reverse of the number is : ',rev)
