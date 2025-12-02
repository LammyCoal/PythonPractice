task = []

def add_task():
    work = input("Which task do you want to add? ")
    task.append(work)
    print(f"Task added: {work}")

def view_tasks():
    if not task:
        print('No tasks available')
        return
    print('\n These are your tasks:')
    for i, work in enumerate(task, 1):
        print(f"{i}. {work}")

def delete_task():
    view_tasks()

    if not task:
        print('No tasks available')
        return

    try:
        numero = int(input("Which task do you want to delete? "))
        if 1 <= numero <= len(task):
            task.pop(numero -1)
        print(f"You deleted {numero} from your tasks")
        print(task)

    except ValueError:
        print("You didn't enter a valid number")


def main():
    while True:
        print('\n --To do list Menu--')
        print('1. View tasks--')
        print('2. Delete tasks--')
        print('3. Add tasks--')
        print('4. Quit--')

        choose = int(input('what would you like to do? '))
        if choose == 1:
            view_tasks()
        elif choose == 2:
            delete_task()
        elif choose == 3:
            add_task()
        elif choose == 4:
            print('Goodbye')
            break
        else:
            print('Invalid input')

main()

