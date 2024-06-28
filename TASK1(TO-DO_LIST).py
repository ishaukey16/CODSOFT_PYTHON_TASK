
tasks = [] #empty list
print("---------WELCOME  TO TO-DO LIST THE TASK MANAGEMENT APP---------")

total_task = int(input("How many task you want to add? = "))#5
for i in range(1,total_task+1):
    task_name = input(f"Enter task {i} = ")
    tasks.append(task_name)

print("\nToday's tasks are:")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

while True:
    print("\n1. Add Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. View Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task = input("Enter task you want to add: ")
        tasks.append(add_task)
        print(f"task '{add_task}' has been successfully added...")

    elif choice == "2":
        update_task = input("Enter task you want to update: ")
        if update_task in tasks:
            update = input("enter new task: ")
            ind = tasks.index(update_task) #2
            tasks[ind] = update
            print(f"Task '{update_task}' has been updated to '{update}'.")
        else:
            print("Task not found.")

    elif choice == "3":
        delete_task = input("which task you want to delete: ")
        if delete_task in tasks:
            ind = tasks.index(delete_task)
            del tasks[ind]
            print(f"task '{delete_task}' has been deleted.")
        else:
            print("Task not found.")

    elif choice == "4":
        print("\nToday's tasks are: ")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif choice == "5":
        print("closing the program..")
        break
    else:
        print("Invalid input.")

