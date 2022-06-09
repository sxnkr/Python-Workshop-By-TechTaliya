#File Handling


#file object =open("<file-name>","<access-mode>")

'''
file = open("file.txt","w")
if file:
   print("File is created successfully")
   file.write("Hello World")
   print(file.closed)
   print(file.mode)
   print(file.name)

#Access modes
r
rb
r+
rb+
w
wb
w+
wb+
a
ab
a+
ab+

#In-Built functions
1.file.closed
>Returns true if file is closed, false otherwise
2.file.mode
>Returns access mode with file was opened
3.file.name
>Returns the name of the file

'''

#Write a file
'''
file = open("file.txt","w")
if file:
   print("File is created successfully")
   file.write("Hello World")
   file = open("file.txt","r")
   print(file)
   file.close()
'''
'''
#append to a file
file = open("file.txt","a")
if file:
   print("File is created successfully")
   file.write("Hello World")
   file = open("file.txt","r")
   print(file.read())
   file.close()


#Read 10 byes
file = open("file.txt","r")
if file:
   print(file.read(10))
   file.close()

# reading the file(line) 

file = open("file.txt","r")
if file:
   print(file.readline())
   file.close()
                                  
#loop through the file (line by line)
file = open("file.txt","r")
if file:
   for i in file:
      print(i)
      print("$")
   file.close()

#OR with statement

with open("file.txt","r") as f:
   print(f.readlines())

file = open("file.txt","r")
if file:
   print(file.tell())
   file.close()

file = open("file.txt","r")
if file:
   print(file.seek(10))
   file.close()

#Renaming file
import os

file = open("file.txt","r")
if file:
   os.rename("file.txt","newfile.txt")
   file.close()
'''
#remove file
import os

os.remove("newfile.txt")



 
