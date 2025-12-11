import os
import json

if os.path.exists("students_data.json"):
    with open("students_data.json", "r") as file:
        students_data = json.load(file)

else:
    students_data = {}

def save_students():
    with open("students_data.json", "w") as f:
        json.dump(students_data, f, indent=4)

def generate_student_id():
    if not students_data:
        return "T001"
    id = [int(sid[1:]) for sid in students_data.keys() if sid.startswith('S')]
    next_id = max(id) + 1

    return f"S{next_id:03d}"

def clean_score_input(text):
    clean = [scores.strip() for scores in text.split(",") if scores.strip() != ""]
    return clean

def average_score(scores):
    return sum(scores) / len(scores)

def grade(scores):
    if scores >= 90:
        return "A"
    if scores >= 80:
        return "B"
    if scores >= 70:
        return "C"
    if scores >= 60:
        return "D"
    if scores >= 50:
        return "E"
    return "F"
