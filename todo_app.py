tasks = [] # create an empty list called tasks

# Make a menu
def show_menu():
    print ("\n---Todo List Menu ---")
    print ("1. View Tasks")
    print ("2. Add Task")
    print ("3. Delete Task")
    print ("4. Exit")
    
def view_tasks():
    if not tasks:
        print ("Your tasks list is empty")
    else:
        print ("\n Your  tasks:")
        for index, task in enumerate(tasks, start = 1):
            print (f"{index}. {task} ")
            
def add_task():
    task = input("Enter a new task")
    tasks.append(task)
    print (f"Task '{task}' added.")
    
def delete_task():
    view_tasks()
    try:
        task_number = int(input("Enter the number to remove the task"))
        task = tasks.pop(task_number - 1)
        print (f"task '{task}' removed.")

    except (IndexError, ValueError):
        print ("Invalid task number")

while True:
    show_menu()
    choice = input("Choose an option (1-4)")
    if choice == '1':
        view_tasks ()
    elif choice == '2':
        add_task ()
    elif choice == '3':
        delete_task ()
    elif choice == '4':
        print ("Goodbye!, see you next time")
else:
    print ("Invalid choice. Please enter a number between 1-4")