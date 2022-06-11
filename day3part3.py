#csv file handling program to print 
import csv
students=[]
with open("./students.csv","r") as file_name:
    file_stream=csv.reader(file_name)
    header = next(file_name)
    header = header.replace('\n','')
    header_list = header.split(',')

    for rows in file_stream:
        obj={}
        for item in header_list:
            pos=header_list.index(item)
            obj[item]=rows[pos]
            #print(obj)
        
        students.append(obj)
    
e_roll=input("Enter the Roll Number:")
error=False
for student in students:
    if student['ROLL NO'] == e_roll:
        print(f"The name of student is {student['NAME']}")
        print(f"The Roll number of student is {student['ROLL NO']}")
        print(f"The Register number of student is {student['REGISTER NO']}")
    
        error=True
        break

if not error:
    print("The record does not exist")
