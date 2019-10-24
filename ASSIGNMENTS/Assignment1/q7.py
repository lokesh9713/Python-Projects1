import calendar

yy = int(input('Enter year: '))
while(yy<=0 or yy>9999):
    print('INVALID YEAR ... Year should be in the range (1-9999) ... Enter again....')
    yy = int(input('Enter year: '))
mm = int(input('Enter month: '))
while(mm<=0 or mm>12):
    print('INVALID MONTH ... Month should be in the range (1-12) ... Enter again....')
    mm = int(input('Enter month: '))

print(calendar.month(yy,mm))


