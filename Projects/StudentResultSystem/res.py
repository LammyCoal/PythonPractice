import os
import json

filename = "students.json"

if os.path.exists("students_data.json"):
    with open("students_data.json", "r") as file:
        students_data = json.load(file)

else:
    students_data = {}

def save_students():
    with open("students_data.json", "w") as f:
        json.dump(students_data, f, indent=4)

def generate_student_ids():
    if not students_data:
        return 'T001'
    id = [int(ids[1:]) for ids in students_data.keys() if ids.startswith("T")]
    next_id = max(id) + 1
    return f"T{next_id:03d}"

def clean_score_input(text):
    clean = [elements.strip() for elements in text if elements.strip() != ""]
    if not clean:
        return None
    scores = []
    for element in clean:
        try:
            answer = float(element)
        except ValueError:
            return None
        if answer < 0 or answer > 100:
            return None
        scores.append(answer)
    return scores

def average_score(scores):
    return sum(scores) / len(scores)

def assign_grade(average):
    if average >= 70:
        return "A"
    if average >= 60:
        return "B"
    if average >= 50:
        return "C"
    if average >= 45:
        return "D"
    if average >= 40:
        return "E"
    else:
        return "F"

def add_students():
    name = input("Enter student's name: ")
    if not name:
        return "Name cannot be empty"

    score_data = input("Enter student scores: ")
    if not score_data:
        return "Scores cannot be empty"
    score_data = clean_score_input(score_data)

    IDs = generate_student_ids()
    average = round(average_score(score_data),2)
    grade = assign_grade(average)

    students_data[IDs] = {
        "name": name,
        "scores": score_data,
        "grade": grade,
        "average": average
    }

    save_students()
    print(f"Student:{name} with grade {grade} sucessfully added ")

def list_students():
    if not students_data:
        print("No students data")
        return
    print(f"{'IDs':10} {'name':20} {'Average':6 } {'Grade':9} ")
    line = ("_" * 50)
    print(line)
    for IDs, data in students_data.items():
        print(f"{IDs:10} {data['name'][:20]:20} {data['average']:6.2f} {data['grade']:9}")
    print()

def student_record(student_id, data):
    print(f"Name: {data['name']}")
    print(f"ID: {student_id}")
    print(f"Average_score: {data['average']:.2f}")
    print(f"Grade: {data['grade']}")

def view_students():
    view = input("Enter student's Id or name to search: ").strip()
    if not view:
        return
    if view in students_data:
        records = students_data[view]
        print(f" Student name is {records['name']}, grade is {records['grade'] }")
        student_record(view, records)
        return

    answer = []
    for ids, data in students_data.items():
        if view.lower() in data['name'].lower():
            answer.append((ids, data))

        if not answer:
            print("no student with that name found")
            return

        for sid, elements in answer:
            student_record(sid, elements)