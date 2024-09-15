from database import tasks
from datetime import datetime, date


def display():
    while True:
        print('---Welcome to ToDo App---')
        print('1. Add Task')
        print('2. Remove Task')
        print('3. View Tasks')
        print('4. Sort by Due Date')
        print('5. Search Task')
        print('6. Display Overdue Tasks')
        print('7. Mark Task as Completed')
        print('8. Exit')
        choice = input('Enter Your Choice(1-8): ').strip()
        choice_manager(choice)


def choice_manager(p1):
        if p1 == '1':
            add_task(tasks)
        elif p1 == '2':
            remove_task(tasks)
        elif p1 == '3':
            view_tasks(tasks)
        elif p1 == '4':
            sort_by_due_date(tasks)
        elif p1 == '5':
            search_task(tasks)
        elif p1 == '6':
            display_overdue_tasks(tasks)
        elif p1 == '7':
            mark_task_as_completed(tasks)
        elif p1 == '8':
            print('Exiting the To-Do Application')
            exit()
        else:
            print('Please enter a number in range 1 to 8.')
        

def add_task(tasks):
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()
    due_date = input("Enter due date(DD-MM-YYYY): ").strip()
    status = "Pending"
    try:
        datetime.strptime(due_date, '%d-%m-%Y')
        tasks[title] = {"description": description, "due_date": due_date, "status": status}
        print(f"Task '{title}' added.")
    except ValueError:
        print('Invalid date format!')


def remove_task(tasks):
    title = input("Enter task title to remove: ")
    if title in tasks:
        del tasks[title]
        print(f"Task '{title}' removed successfully.")
    else:
        print(f"Task '{title}' not found.")


def view_tasks(tasks):
    if tasks:
        print('---All Tasks---')
        for title, details in tasks.items():
            print(f"  Title: {title}")
            print(f"  Description: {details['description']}")
            print(f"  Due Date: {details['due_date']}")
            print(f"  Status: {details['status']}\n")
    else:
        print("No tasks found.")


def sort_by_due_date(tasks):
    if tasks:
        print("\n--- Tasks Sorted by Due Date ---")
        sorted_tasks = sorted(tasks.items(), key=lambda x: x[1]['due_date'])
        for title, details in sorted_tasks:
            print(f"  Title: {title}")
            print(f"  Description: {details['description']}")
            print(f"  Due Date: {details['due_date']}")
            print(f"  Status: {details['status']}\n")
    else:
        print("No tasks found.")


def search_task(tasks):
    search_term = input("Enter part of the task title to search: ").strip()
    found = False
    for title, details in tasks.items():
        if search_term.lower() in title.lower():
            print(f"\n--- Found Task ---")
            print(f"  Title: {title}")
            print(f"  Description: {details['description']}")
            print(f"  Due Date: {details['due_date']}")
            print(f"  Status: {details['status']}\n")
            found = True
    if not found:
        print("No matching tasks found.")    


def display_overdue_tasks(tasks):
    if tasks:
        print("\n--- Overdue Tasks ---")
        today = date.today()
        found = False
        for title, details in tasks.items():
            due_date = datetime.strptime(details['due_date'], '%d-%m-%Y').date()
            if due_date < today and details['status'] != 'Completed':
                details['status'] = 'Failed'
                print(f"  Title: {title}")
                print(f"  Description: {details['description']}")
                print(f"  Due Date: {details['due_date']}")
                print(f"  Status: {details['status']}\n")
                found = True
        if not found:
            print("No overdue tasks.")
    else:
        print("No tasks found.")


def mark_task_as_completed(tasks):
    title = input("Enter task title to mark as completed: ").strip()
    if title in tasks:
        tasks[title]['status'] = 'Completed'
        print(f"Task '{title}' marked as completed.")
    else:
        print(f"Task '{title}' not found.")


if __name__ == '__main__':
    display()
