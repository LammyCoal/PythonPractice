names = []

def grading():
    student_name = input("What is your name? ")
    student_score = int(input("What is your score? "))

    students = {
        "name": student_name,
        "score": student_score
    }


    names.append(students)
    print(f"Your name is {students['name']} and score is {students['score']}")

while True:
    inputs = input('Do you want to continue? (Y/N) ')
    if inputs.lower() == 'y':
        grading()
    elif inputs.lower() == 'n':
        break

print(names)