from math import *
marks = []
serial = ['first','second','third','fourth','fifth']
for i in range(0,5):
    print('Enter marks of the ',serial[i],' subject: ',end='')
    marks.append(float(input()))
avg = fsum(marks)/5
print('Grade: ',end='')
if(avg >= 90 and avg <= 100):
    print('A')
elif(avg >= 80 and avg < 90):
    print('B')
elif(avg >= 60 and avg < 80):
    print('C')
elif(avg >= 40 and avg < 60):
    print('D')
elif(avg >= 0 and avg < 40):
    print('F')
else:
    print('There is some error in the data!!!')

    