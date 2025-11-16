import os
def load_tasks():
#ye file se task load krega agar nahi krta exist then it will send empty list 
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]
#ye task save krega
def save_tasks(tasks):
    """Saves current tasks to file."""
    with open(FILENAME, "w") as file:
        for t in tasks:
            file.write(t + "\n")
    print("✔ Tasks saved successfully.\n")
#ye menu display krega
def display_menu():
    print("\n=========== TO DO LIST ============")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Save changes")
    print("5. Create NEW to-do list (overwrite)")
    print("6. Exit")
    print("===================================\n")
#ye task display krega
def display_list(tasks):
    if not tasks:
        print("No tasks in the list.\n")
    else:
        print("\nCurrent Tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
        print()
#ye task add krega
def add_task(tasks):
    new_task = input("Enter the new task: ").strip()
    if new_task:
        tasks.append(new_task)
        print(f"✔ Task '{new_task}' added.\n")
#ye task remove krega
def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.\n")
        return
    display_list(tasks)
    try:
        index = int(input("Enter task number to remove: "))
        removed = tasks.pop(index - 1)
        print(f"✔ Removed: {removed}\n")
    except:
        print("Invalid choice.\n")
#ye naya list create krega
def create_new_list():
    """Overwrites old file by clearing tasks."""
    confirm = input("Are you sure you want to create a NEW list? (y/n): ")
    if confirm.lower() == 'y':
        save_tasks([])   # empty new list
        print("New empty to-do list created.\n")
        return []
    else:
        print("Cancelled.\n")
        return None
#ye main function hai jo program run krega
def todolist():
    tasks = load_tasks()
    print("Your to-do list has been loaded.\n")
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            display_list(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
        elif choice == '5':
            new_list = create_new_list()
            if new_list is not None:
                tasks = new_list.copy()   # using copy()
        elif choice == '6':
            print("Thanks, come back again!")
            break
        else:
            print("Invalid choice, try again.\n")



if __name__ == "__main__":
    FILENAME = "todolist.txt"
    todolist()
