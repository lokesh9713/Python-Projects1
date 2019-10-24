#1)LCM
'''def lcm(a,b):
    if(a>b):
        larger=a
    else:
        larger=b
    while(a>0 or b>0):
        if((larger%a==0) and (larger%b==0)):
            l=larger
            break
        larger+=1
    return l
x=int(input("enter first number:"))
y=int(input("enter second number:"))4ee
print("LCM of",x,"and",y,"is",lcm(x,y))
'''



#2)HCF
'''def gcd(a,b):
    if(a==b):
        smaller=a
    elif(a<b):
        smaller=a
    elif(a>b):
        smaller=b
    for i in range(1,smaller+1):
        if((a%i==0) and (b%i==0)):
            g=i
    return g
x=int(input("enter first number:"))
y=int(input("enter second number:"))
print("GCD of",x,"and",y,"is",gcd(x,y))
'''            
 
 
 
#3)Calculator
'''def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mult(a,b):
    return (a*b)
def div(a,b):
    return (a/b)
print("select option: ")
print("1.Add\n2.Subtraction\n3.Multiplication\n4.Division")
x=int(input("enter first number: "))
y=int(input("enter second number: "))
ch=int(input("enter choice(1/2/3/4): "))
if(ch==1):
    print(x,'+',y,'=' ,add(x,y))
elif(ch==2):
    print(x,'-',y,'=' ,sub(x,y))
elif(ch==3):
    print(x,'*',y,'=' ,mult(x,y))
elif(ch==4):
    print(x,'/',y,'=' ,div(x,y))
else:
    print("Invalid input")                
'''




#4)Fibonacci using Recursion
'''def fib(a):
    if(a==0):
        return a
    elif(a<=1):
        return a
    else:
        return (fib(a-1)+fib(a-2))
n=int(input("enter number of terms: "))
print("Fibonacci series: ",end='')
for i in range(n):
    print(fib(i),end=' ')
'''    
        





#5)Factorial using Recursion
'''def fact(a):
    if(a<=1):
        return 1
    else:
        return (a*fact(a-1))
b=int(input("enter number whose factorial is to be found: "))
print("Factorial is: ",end='')
print(fact(b))
'''




#6)Decimal to Binary and Octal to Hexadecimal
#Decimal to Binary
'''def dec2bin(a):
    l=[]
    c=a
    while(c>0):
        b=c%2
        l.append(b)
        c=c//2
    return (l) 
n=int(input("enter a decimal number: "))
l=dec2bin(n)
print("\ndecimal to binary=",end='')
for i in l[::-1]:
    print(i,end='')
'''
#Octal to Hexadecimal
'''print("enter 'x' for exit")
octal=input("enter a number in octal format: ")
if(octal=='x'):
    exit()
else:
    dec=str(int(octal))   #converted into a string to obtain every digit of ocatl
    #print(dec[0])
    #print(dec)
    decm=int(dec)
    #print(decm)
    print(octal,"in hexadecimal=",hex(decm))
'''




#7)Sort words in alphabetical order
words=input("enter words to be sorted: ")
w=words.split()
#print (w)
w.sort()
for word in w:
    print(word,end=' ')           
            
    
    
                                    