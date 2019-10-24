num = int(input('Enter a number: '))
list1=[]
num1=num
while(num1>0):
    rem = num1 % 10
    list1.append(rem)
    num1 //= 10
n = len(list1)-1
rev = 0
for val in list1:
     rev += val*(10**n)
     n = n-1
if(num == rev):
    print('Pallindrome')
else: 
    print('Not pallindrome')
