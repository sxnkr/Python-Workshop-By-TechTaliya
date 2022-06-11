import csv

students= []
with open('./students.csv','r') as file_name:
    file_stream = csv.reader(file_name)
    header = next(file_name)
    
    header = header.replace('\n','')
    header_list = header.split(',')
    for row in file_stream:
        obj = {}
        for item in header_list:
            pos = header_list.index(item)
            obj[item] = row[pos]
       
        students.append(obj) 

roll_no = input("please enter the roll no :")
found = False
for student in students:
    if student['ROLL NO'] == roll_no:
        print("The student details are")
        print("ROLL NO : ",student['ROLL NO'])
        print("Register Number : ",student['REGISTER NO'])
        print("NAME : ", student['NAME'])
        found = True
        break
if not found:
    print("no such roll number found in the file")
