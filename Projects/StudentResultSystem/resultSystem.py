import os
import json

name = input("Enter student name: ")
english = int(input("Enter english grade: "))
maths = int(input("Enter maths grade: "))
physics = int(input("Enter physics grade: "))
chemistry = int(input("Enter chemistry grade: "))
average = (english + maths + physics + chemistry)/ 4

filename = "students.json"
if os.path.exists(filename):
    with open(filename, 'r') as file:
        students = json.load(file)
else:
    students = {}

students[name] = {
    'english': english,
    'maths': maths,
    'physics': physics,
    'chemistry': chemistry,
    'average': average,
    'grades': ''
}

# Main menu

if average >= 70:
    students[name]['grades'] = 'A'
elif average >= 60:
    students[name]['grades'] = 'B'
elif average >= 50:
    students[name]['grades'] = 'C'
elif average >= 45:
    students[name]['grades'] = 'D'
elif average >= 40:
    students[name]['grades'] = 'E'
elif average < 40:
    students[name]['grades'] = 'F'


with open(filename, 'r+') as file:
    json.dump(students, file, indent=4)
