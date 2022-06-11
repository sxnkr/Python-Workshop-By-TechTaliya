#python for loop

for i in range(0,10):
   print(i,end=' ')
for i in range(0,10):
   print(i,end='\n')


#Multiplication Table
n=int(input("Enter the number:"))
for i in range(1,11):
   print("%dX%d=%d"%(n,i,n*i))

#Nested loop
for i in range(0,10):
   print(i,end=' ')
   for j in range(0,10):
      print(j,end='\n')


#using else with for loop

for i in range(0,5):
   print(i)
# `  break;
else:
   print("For loop finished");
print("break statement")


#While loop
#Multiplication Table
i=1
n=int(input("Enter the number:"))
while i<=10:
   print("%dX%d=%d"%(n,i,n*i))
   i+=1


#Infinte while loop

while(1):
   print("Hey man wassup yoh")


#Continue loop
i=0
for i in range(0,5):
   print("Hey man wassup yoh")
   if i==3:
      continue;
   print("continue")





