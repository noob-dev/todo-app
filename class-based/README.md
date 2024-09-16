# To-Do List Application

## Objective
The objective of this program is to create a simple To-Do list application that allows users to manage tasks using various data structures and control flow mechanisms.

## Features
1. **Add Task**: Users can add tasks to their to-do list. Each task consists of a title, description, due date, and status.
2. **Remove Task**: Users can remove tasks from their to-do list based on the task title.
3. **View Tasks**: Users can view all tasks in their to-do list, displayed in a formatted manner.
4. **Sort by Due Date**: Users can view tasks sorted by due date, with earlier due dates displayed first.
5. **Search Task**: Users can search for tasks based on partial matches of the title.
6. **Display Overdue Tasks**: Users will receive notifications for tasks that are overdue, and their status will be automatically updated to "Failed".
7. **Mark Task as Completed**: Users can mark a task as completed, changing its status to "Completed".
8. **Persistent Storage**: Tasks are saved to a JSON file and loaded when the program starts, ensuring data persistence between runs.

## Data Structures Used
- **Dictionary**: To store task details, with task titles as keys.
- **List**: To store sorted tasks for displaying sorted tasks by due date.

## Control Flow
- **While Loop**: Used for providing a menu-driven interface and for the main program loop.
- **Conditional Statements**: Used for implementing various functionalities like adding tasks, removing tasks, sorting tasks, searching tasks, updating task status, displaying tasks, and exiting the program.

## User Interface
The program provides a command-line interface (CLI) for users to interact with. Users are presented with a menu of options to choose from, such as adding tasks, removing tasks, viewing tasks, sorting tasks, searching tasks, updating task status, displaying overdue tasks, marking tasks as completed, and exiting the program.

## Error Handling
The program handles invalid user input gracefully, providing appropriate error messages and prompting the user to input valid data.

## Dependencies
- The program is developed using Python programming language.
- No external libraries are used, relying only on built-in data structures and control flow mechanisms.

## How to Run
1. Ensure you have Python installed on your system.
2. Download the `todo_list.py` file.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `todo_list.py`.
5. Run the program using the command:
   ```sh
   python todo_list.py
