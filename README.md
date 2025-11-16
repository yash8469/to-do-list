To-Do List Program
This project is a simple command-line To-Do List manager written in Python. The goal was to build a program that can handle real-world list operations such as creating a new list, loading an existing one, adding tasks, removing tasks, and saving changes to a file.
The program stores all tasks in a text file (todolist.txt) and allows the user to rewrite, update, or completely recreate the list whenever needed.
What This Program Can Do
1. Load an Existing To-Do List
When the program starts, it checks if the file already exists. If it does, the list is loaded and displayed to the user.
2. Create a New To-Do List
The user can choose to create an entirely new list. This option overwrites the previous file and starts with an empty list.
3. Add Tasks
Tasks can be added one by one. Each added task updates the list stored in memory.
4. Remove Tasks
The program shows the list with numbering, allowing the user to remove a task by entering its index.
5. Save Changes
Any time during use, the user can decide to save the updated or modified task list back to the file.
6. Exit Safely
The user can exit the program without saving if they want. The program keeps things simple and does not force overwriting unless the user confirms.
What I Researched
While creating this project, I explored:
How to read from and write to files using Python’s open() function
How to check whether a file exists using os.path.exists()
Best practices for handling lists inside programs
The use of helper functions to keep the code organized and readable
How to safely overwrite files without accidental data loss
When and why to use copy() for lists
Structuring a menu-driven program using loops and conditional statements
What I Used in This Program
Python file handling (read, write, and overwrite operations)
Lists for storing tasks
The os module to check file availability
Clean modular functions such as load_tasks(), save_tasks(), add_task(), and remove_task()
A menu-driven loop to navigate between different features
Error handling for invalid inputs
Basic list methods including append(), pop(), and copy()
(A file named todolist.txt will be created automatically if it doesn’t already exist.)
