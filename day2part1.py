#Day 2 of python workshop
'''input function'''
#To read a value from the user

value=input("Enter a value:")
#Now printing the value
print(value)
print(type(value))

#The input function reads the value entered and store it as string.
#So if one wants to add or do any kinds of arithmetic operation one should type cast it.

a=int(input("Enter the value a:"))
b=int(input("Enter the value of b:"))
print("Sum of a and b is:",a+b)


#Python String
#A collection of characters is a string
#Can be rep using "" , '' etc
#string is a ordered data(In a particular way)
#Like an array in C

#Slice operator( [] ) is user to access  the individual characters of the string

stringtest="GovindSankar"

print(stringtest[0])
print(stringtest[1])
print(stringtest[2])
print(stringtest[3])
print(stringtest[4])

#[<start index>:<End index>]
print(stringtest[:10])
#Here the string is printing fron 0 to 10. Their is no need for specifing the start index.If not specified the start inderx is taken as 0.
#Example 2
print(stringtest[2:5])
#Here the string is printed from 2 to 5 only(2 is included but 5 is not).

#strings are immutable. Reassigning the value as a whole is possible. But cannot change or modifiy a inputed string.

'''Python Data Strucutes'''

'''Python List'''

#A list can be defined as a collection of value of same of different data types, the values are separated by commas in a square brackets( [] ).
#Example1
list1=[0,1,2,3,4,5,6,7,8,9]

#list acts like a string, Indexing princlples are the same.
print(list1[3:8])
#Same as string, start in on ex is included but end index is not.
#The end index should be less than or equal to the max number of items.
#We can also index negatively like [5:-2]

print(list1[3:-1])

#List is mutable
#The values of the list can be updated by using slice and assignment operator.

print(list1)

list1[5]=1.6
list1[3]='vdv'
#here the 5 itemm on the list is updated by abco.
print(list1)

# We can also append the list
#By using <name of the list>.append 
#example
list1.append(123)

#Deleting or removing the item at 4th position
del list1[4]
print(list1)

list1[1:3]=[324,341]

list1.remove(3)

print(list1)

'''Python list op'''

'''
1.Repetition
>It enable the list elements to be repeated multiple times.(L1*2)
2.Concatination
>It enable the concatination or joining of two seprate list into one.(l1+l2)
3.Membership
>It returns true if a particular item exits in a list.Otherwise false
4.Iteration
>The for loop is used to iterate over the list elements.
for i in l1:
  print(i)
5.Length
>It is used to get the length of the list
len(l1)
'''

#Python Built-in fun
'''
1.cmp(l1,l2)
>It compares the elements of the both the lists.
2.len(list)
It used to calculate the the length of the list.
3.max(list)
It returns the maximum element of the list. 
4.min(list)
It returns the minimum element of the list.
5.list(seq)
It convets seq into list.
'''
l1=[1,2,3,4]
l2=[4,5,6,7]
print(cpm(l1,l2))







