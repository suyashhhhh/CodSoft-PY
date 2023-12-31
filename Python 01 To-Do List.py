#Task01
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task Completion")
    print("4. Quit")

def view_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "Completed" if task[1] else "Pending"
            print(f"{index}. {task[0]} [{status}]")

def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list.append([task, False])
    print("Task added successfully!")

def update_task(todo_list):
    view_todo_list(todo_list)
    if not todo_list:
        return

    try:
        task_number = int(input("\nEnter the task number to update: "))
        if 1 <= task_number <= len(todo_list):
            _, status = todo_list[task_number - 1]
            if not status:
                todo_list[task_number - 1][1] = True
                print("Task marked as completed!")
            else:
                print("Task is already completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    todo_list = []

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                view_todo_list(todo_list)
            elif choice == 2:
                add_task(todo_list)
            elif choice == 3:
                update_task(todo_list)
            elif choice == 4:
                print("Exiting the To-Do List Application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
