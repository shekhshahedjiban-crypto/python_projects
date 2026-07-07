def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def main():
    tasks = []  # List to store the tasks
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == "1":
            if not tasks:
                print("\nYour to-do list is empty!")
            else:
                print("\nYOUR TASKS:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                    
        elif choice == "2":
            new_task = input("\nEnter the task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"'{new_task}' has been added.")
            else:
                print("Task cannot be empty!")
                
        elif choice == "3":
            if not tasks:
                print("\nNo tasks to delete.")
            else:
                print("\nYOUR TASKS:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                
                try:
                    task_num = int(input("\nEnter the number of the task to delete: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        print(f"'{removed}' has been deleted.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
                    
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Please choose between 1 and 4.")

if __name__ == "__main__":
    main()