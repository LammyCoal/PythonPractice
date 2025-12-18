import os
import json

filename = "students_data.json"

if os.path.exists("students_data.json"):
    with open("students_data.json", "r") as file:
        students_data = json.load(file)
else:
    students_data = {}


def save_students():
    with open("students_data.json", "w") as f:
        json.dump(students_data, f, indent=4)


def generate_student_ids(students_data):
    IDS = [int(ids[1:]) for ids in students_data.keys() if ids.startswith("T") and ids[1:].isdigit()]
    if not IDS:
        return "T001"
    next_id = max(IDS) + 1
    return f"T{next_id:03d}"


def clean_score_input(text):
    clean = [elements.strip() for elements in text.split(",") if elements.strip() != ""]
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
    if score_data is None:
        print("Invalid Score Input")
        return

    IDs = generate_student_ids(students_data)
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
    print(f"{'IDs':10} {'name':20} {'Average':6} {'Grade':9} ")
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


def edit_students():
    Student_id = input("Enter student's Id to edit: ").strip()
    if Student_id not in students_data:
        print("no student with that name found")
        return
    records = students_data[Student_id]
    print("current records:")
    student_record(Student_id, records)

    if Student_id in students_data:
        change = input("""
        what do you want to change?.
        1. Name
        2. Scores
        3. Both
        4. Cancel
        """)
        if change in ("1","3"):
            students_data[Student_id]["name"] = input("Enter new name: ")

        if change == ("2","3"):
            raw = input("Enter new scores: ")
            cleaned = clean_score_input(raw)

            if cleaned is None:
                print("Invalid Scores input, please try again")
                return
            students_data[Student_id]["scores"] = cleaned
            records["average"] = round(students_data[records]["average"], 2)
            records["grade"] = assign_grade(records["average"])

            students_data[Student_id] = records
            save_students()
            print("Student data updated")
            return
        if change == "4":
            print("Canceled")
            return


def delete_student():
    view = input("Enter student's Id to delete: ").strip()
    if view not in students_data:
        print("no student with that id found")
        return
    confirm = input("Are you sure you want to delete this student? (y/n)")

    if confirm == "y":
        print(f"Deleting {students_data[view]['name']}...")
        del students_data[view]
        save_students()
    else:
        print("Aborted")


def main_menu():
    while True:
        print("\n Welcome to Student Result System")
        print()
        print("""
        Student Management System
        1. Add Student
        2. List Students
        3. Edit Student
        4. Delete Student
        5. View Students
        6. Exit
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            add_students()
        elif choice == "2":
            list_students()
        elif choice == "3":
            edit_students()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            view_students()
        elif choice == "6":
            print("Thanks for using Student Result System, Goodbye")
            break
        else:
            print("Invalid choice, please try again")


if __name__ == "__main__":
    main_menu()

