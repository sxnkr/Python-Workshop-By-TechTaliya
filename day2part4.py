#Conditional Statements
#If Statement
num=int(input("Enter the num: "))
if num%2==0:
   print("Number is even")
else :
   print("Number is odd")

#Multiple condition in one if

a = int(input("Enter a?"))
b = int(input("Enter b?"))
c = int(input("Enter c?"))

if a>b and a>c :
   print("A is the largest")
if b>a and b>c :
   print("b is the largest")
if 	c>b and c>a :
   print("C is the largest")
#if-elif-else statement
a = int(input("Enter a?"))
b = int(input("Enter b?"))
c = int(input("Enter c?"))

if a>b and a>c :
   print("A is the largest")
elif b>a and b>c :
   print("b is the largest")
else      c>b and c>a :
   print("C is the largest")


