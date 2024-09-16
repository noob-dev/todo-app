from datetime import datetime
import json


class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Pending"

    def mark_completed(self):
        self.status = "Completed"

    def is_overdue(self):
        current_date = datetime.now().strftime("%d-%m-%Y")
        if self.due_date < current_date and self.status != "Completed":
            self.status = "Failed"
            return True
        return False

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["title"], data["description"], data["due_date"])
        task.status = data["status"]
        return task

class ToDoList:
    def __init__(self):
        self.tasks = {}
        self.load_tasks()

    def add_task(self, title, description, due_date):
        if title in self.tasks:
            print(f"Task '{title}' already exists.")
        else:
            self.tasks[title] = Task(title, description, due_date)
            print(f"Task '{title}' added successfully.")
            self.save_tasks()

    def remove_task(self, title):
        if title in self.tasks:
            del self.tasks[title]
            print(f"Task '{title}' removed successfully.")
            self.save_tasks()
        else:
            print(f"Task '{title}' not found.")

    def view_tasks(self):
        if self.tasks:
            for task in self.tasks.values():
                task.is_overdue()  # Update status if overdue
                self.display_task(task)
        else:
            print("No tasks found.")

    def sort_by_due_date(self):
        sorted_tasks = sorted(self.tasks.values(), key=lambda x: x.due_date)
        for task in sorted_tasks:
            task.is_overdue()  # Update status if overdue
            self.display_task(task)

    def search_task(self, search_term):
        found_tasks = [task for task in self.tasks.values() if search_term.lower() in task.title.lower()]
        if found_tasks:
            for task in found_tasks:
                task.is_overdue()  # Update status if overdue
                self.display_task(task)
        else:
            print("No tasks found.")

    def display_overdue_tasks(self):
        overdue_tasks = [task for task in self.tasks.values() if task.is_overdue()]
        if overdue_tasks:
            for task in overdue_tasks:
                self.display_task(task)
        else:
            print("No overdue tasks found.")

    def mark_task_completed(self, title):
        if title in self.tasks:
            self.tasks[title].mark_completed()
            print(f"Task '{title}' marked as completed.")
            self.save_tasks()
        else:
            print(f"Task '{title}' not found.")

    def display_task(self, task):
        print(f"\nTitle: {task.title}")
        print(f"Description: {task.description}")
        print(f"Due Date: {task.due_date}")
        print(f"Status: {task.status}")

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump({title: task.to_dict() for title, task in self.tasks.items()}, file)

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                tasks_data = json.load(file)
                self.tasks = {title: Task.from_dict(data) for title, data in tasks_data.items()}
        except FileNotFoundError:
            self.tasks = {}

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Sort by Due Date")
        print("5. Search Task")
        print("6. Display Overdue Tasks")
        print("7. Mark Task as Completed")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (DD-MM-YYYY): ")
            todo_list.add_task(title, description, due_date)
        
        elif choice == '2':
            title = input("Enter task title to remove: ")
            todo_list.remove_task(title)
        
        elif choice == '3':
            todo_list.view_tasks()
        
        elif choice == '4':
            todo_list.sort_by_due_date()
        
        elif choice == '5':
            search_term = input("Enter task title to search: ")
            todo_list.search_task(search_term)
        
        elif choice == '6':
            todo_list.display_overdue_tasks()
        
        elif choice == '7':
            title = input("Enter task title to mark as completed: ")
            todo_list.mark_task_completed(title)
        
        elif choice == '8':
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
