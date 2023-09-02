# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

# Function to remove a task
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found!")

# Function to display the list of tasks
def show_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Main program loop
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show tasks")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
