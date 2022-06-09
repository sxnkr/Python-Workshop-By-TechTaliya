#Pass Statement

#In python, pass keyword is used to exectute a block




#Function

#in python we use def keyword to define a function
'''
def my function():
   < function body >
   return <expression>

def hellow():
   print("Hello World")

hellow()

#sum
def sum(a,b):
  return a+b;

a=int(input("Enter A:"))
b=int(input("Enter B:"))

print("Sum = ",sum(a,b))


'''
'''
#Variable lengh arguments(any no of arguments)

#sum
nos=(1,2,3,4,5,6,7,8,9)
def sum(*a):
   print(type(a))
   for i in a:
      s=s+i

print("Sum = ",sum(nos))

'''




