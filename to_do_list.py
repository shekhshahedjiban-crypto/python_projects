def show_menu(): #def show_menu() for displaying the menu for every loop
    print("\n    Jiban's to do list    ")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def main(): #def main() for storing the task list
    tasks = []
    
    while True: #while_True is used for infite loop untill break statement occurs
        show_menu()
        choice = input("\nChoose an option (1-4): ")
        #option 1 is view task
        if choice == "1":
            if len(tasks) == 0: #checking the list of task is equal to zero or not
                print("\nYour to do list is empty!")
            else:
                print("\nYour tasks:")
                serial_no = 1  #counting starts from 1 in serial_no variable
                for task in tasks:
                    print(f"{serial_no} {task}") #print function for printing serial no and task sidewise
                    serial_no += 1 #serial number will increase in every loop
                    
        #option 2 is add task
        elif choice == "2":
            new_task = input("\nEnter the task: ")
            if new_task:
                tasks.append(new_task)#new task will be added at the end of the list
                print(f"'{new_task}' has been added.")
            else:
                print("Task cannot be empty!")
                
        #option 3 is delete task
        elif choice == "3":
            if len(tasks) == 0: #checking if there is anything to delete in the task list
                print("\nNo tasks to delete.")
            else:
                print("\nYOUR TASKS:") #viewing task list before deleting
                serial_no = 1 #same code as option 1 which indicates view task
                for task in tasks:
                    print(serial_no, task)
                    serial_no += 1
                
                try:
                    task_num = int(input("\nEnter the number of the task to delete: "))
                    #taking input of which task to delete in task_num variable
                    if 1 <= task_num <= len(tasks):
                        #checking whether the input number of deleting task is in between one and len(tasks)
                        remove = tasks.pop(task_num - 1)#tasks.pop is used for deleting task from tasks list []
                        #python starts counting from zero, that's why subtracting one to delete the original task as task counting starts from one in serial_no variable
                        print(f"'{remove}' has been deleted.")
                    else: #if the input number of deleting task is not between the range of one to len(tasks)
                        print("Invalid task number.")
                except ValueError:#except value error handles the unwanted input value from the user
                    print("Please enter a valid number.")
                    
        #option 4 is exit
        elif choice == "4":
            print("\nGoodbye!") #prints goodbye message before exit
            break #breaks the loop for exit
        else:#handles the unwanted input number value from user which are not in range of one to four
            print("Invalid choice! Please choose between 1 and 4.")#shows warning message to the user

if __name__ == "__main__":
    #this check ensures the program only runs if the file is executed directly
    main()