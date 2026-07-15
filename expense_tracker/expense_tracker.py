class Expense:
    def __init__(self, expense_id, date, category, amount, description):
        #function that contain expense id,date,category,amount,description for object's property
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

    def display_info(self):
        return f"ID: {self.expense_id} | Date: {self.date} | Category: {self.category} | Amount: ${self.amount:.2f} | Desc: {self.description}"
    #function for returning expense's all information in text form


class ExpenseTrackerSystem:
    def __init__(self, budget=0.0):
        self.budget = budget
        self.expenses = {}  
#function for creating blank dictionary named self.expenses to store expense's information

    def add_expense(self): #function for adding expense
        print("\n    Add New Expense    ")
        expense_id = input("Enter Expense ID: ")
        #checking if the expense id is already exist in the system
        if expense_id in self.expenses:
            print("Error: An expense with this ID already exists.")
            return #for using return loop will be start again for asking expense id input     
        
        date_str = input("Enter Date (e.g., 2026-07-12): ")
        #taking input of date from user manually as string
        category = input("Enter Category (e.g., Food, Rent): ")
        #taking input of expense category
        
        try:
            amount = float(input("Enter Amount Spent: $"))
            #taking input of amount and convert it to float for calculation
        except ValueError:
            print("Error: Please enter a valid number for the amount.")
            return #return is used for restart the loop asking for expense id

        description = input("Enter Description/Notes: ")
        #taking input of description or notes about the expense

        if len(expense_id) == 0 or len(category) == 0 or len(date_str) == 0:
            #len() is used for checking the expense id, date or category is empty or not
            print("Error: ID, Date and Category cannot be empty.")
            return #return is used for restart the loop asking for inputs

        if amount <= 0:
            #checking if the inputted amount is greater than zero or not
            print("Error: Expense amount must be greater than zero.")
            return #return is used for restart the loop if amount is 0 or negative

        new_expense = Expense(expense_id, date_str, category, amount, description)
        #expense's information is storing in new_expense object by calling Expense class that created at the starting of code
        
        self.expenses[expense_id] = new_expense
        #new_expense object is assigning to self.expenses dictionary with [expense_id] key
        print(f"Success: Added ${amount:.2f} under '{category}' successfully!")
        #output message of inputted expense's category added successfully

    def view_summary(self): #function for viewing expense summary report
        print("\n    Expense Summary Report    ")
        if len(self.expenses) == 0:
            #len() is used to check self.expenses{} dictionary is empty or not
            print("No expenses recorded yet.")
            return #return for back to the loop again
        
        print(f"{'ID':<6} | {'Date':<12} | {'Category':<12} | {'Amount':<10} | {'Description'}")
        print("-" * 65) #printing table design separator lines
        
        total_spent = 0.0 #initializing total_spent variable with 0.0 value to calculate total expense
        for expense_id in self.expenses: #starting loop if expense_id is in self.expenses {} dictionary
            expense = self.expenses[expense_id]
            #extracting specific expense from self.expenses{} dictionary by using [expense_id] key and save it in expense object
            print(f"{expense.expense_id:<6} | {expense.date:<12} | {expense.category:<12} | ${expense.amount:<9.2f} | {expense.description}")
            #printing expense information details step by step using dot with formatted text structure
            total_spent += expense.amount
            #adding current expense amount to total_spent variable in every loop execution
            
        print("-" * 65) #printing table design separator lines
        print(f"Total Amount Spent: ${total_spent:.2f}")
        #printing the final calculated total amount spent till now
        
        if self.budget > 0: #checking if the budget was set greater than zero or not
            remaining = self.budget - total_spent
            #calculating remaining budget by subtracting total_spent from self.budget
            print(f"Remaining Budget:   ${remaining:.2f}")
            #printing remaining budget value
            if remaining < 0: #checking if the remaining budget value is less than zero (negative)
                print(" Warning: You have exceeded your budget!")
                #showing warning message if user cross their monthly budget limit

    def search_expense(self): #function for searching expenses
        print("\n     Search Expense     ")
        expense_id = input("Enter Expense ID to search: ")
        #taking input of expense id for searching expense
        if expense_id in self.expenses:#starting loop if expense_id is in self.expenses {} dictionary
            print("\nExpense Found.")
            print(self.expenses[expense_id].display_info())
            #printing expense's information using [expense_id] key in self.expenses dictionary and entering display_info() function by dot
        else:
            print("Expense not found.") #if inputted expense_id is not in the dictionary

    def delete_expense(self):#function for deleting expenses
        print("\n    Delete Expense Record    ")
        expense_id = input("Enter Expense ID to delete: ")
        if expense_id in self.expenses: #starting loop if expense_id is in self.expenses {} dictionary
            removed_expense = self.expenses.pop(expense_id)
            #entering self.expenses{} dictionary by expense_id key to pop/delete by pop() function and store it temporary in removed_expense object
            print(f"Expense ID '{removed_expense.expense_id}' record deleted successfully.")
            #printing the expense's id by removed_expense object entering to expense_id by dot and that was previously stored by dictionary{}
        else:
            print("Expense ID not found.") #if inputted expense id is not in the dictionary{}


def main(): #the main function that controls the execution of the entire program
    print("    Welcome to jiban's expense tracker    ")
    try:
        budget_input = input("Enter your monthly budget limit (or press Enter for no limit): ").strip()
        #taking input from user for setting up monthly budget limit 
        budget = float(budget_input) if budget_input else 0.0
        #if input is given then converting to float, otherwise assigning default 0.0 value
    except ValueError:
        print("Invalid input. Starting with no budget limit.")
        budget = 0.0 #setting default budget 0.0 if user inputs an invalid text or character

    ets = ExpenseTrackerSystem(budget) #created an object of the ExpenseTrackerSystem class called ets
    
    while True: #starting the infinite loop until the user exit
        print("\n Welcome to jiban's expense tracker system")
        print("1. Add expense")
        print("2. View expense summary")
        print("3. Search expense by id")
        print("4. Delete expense")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ")
        #taking input from user to choose an menu option between 1 to 5
        
        if choice == "1":
            ets.add_expense() #calling add_expense() function from ets object if choice is 1
        elif choice == "2":
            ets.view_summary() #calling view_summary() function from ets object if choice is 2
        elif choice == "3":
            ets.search_expense() #calling search_expense() function from ets object if choice is 3
        elif choice == "4":
            ets.delete_expense() #calling delete_expense() function from ets object if choice is 4
        elif choice == "5":
            print("\nExiting system. Stay on top of your financial goals! Goodbye!")
            break #breaking the infinite while loop to close the program execution
        else:
            print("Invalid choice! Please select a number between 1 and 5.")
            #printing error message if choice input is anything else outside 1 to 5

if __name__ == "__main__": #checking if this script is being run directly as the main program
    main()  #calling the main function to start the execution of the program
