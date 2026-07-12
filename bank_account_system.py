class Account:
    def __init__(self, account_no, holder_name, account_type, balance=0.0):
        #function that contain account no,holder name,account type,balance for object's property
        self.account_no = account_no
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = float(balance)

    def display_info(self):
        return f"Acc No: {self.account_no} | Holder: {self.holder_name} | Type: {self.account_type} | Balance: ${self.balance:.2f}"
    #function for returning account's all information in text form


class BankManagementSystem:
    def __init__(self):
        self.accounts = {}  
#function for creating blank dictionary named self.accounts to store account's information

    def add_account(self): #function for adding account
        print("\n    Create New Bank Account    ")
        account_no = input("Enter Account Number: ")
        #checking if the account number is already exist in the system
        if account_no in self.accounts:
            print("Error: An account with this number already exists.")
            return #for using return loop will be start again for asking account no input     
        holder_name = input("Enter Account Holder Name: ")
        account_type = input("Enter Account Type (Savings/Current): ")
        
        try:
            initial_deposit = float(input("Enter Initial Deposit Amount: $"))
        except ValueError:
            print("Error: Please enter a valid number for deposit.")
            return #return is used for restart the loop asking for inputs

        if len(account_no) == 0 or len(holder_name) == 0:
            #len() is used for checking the account no or holder name is empty or not
            print("Error: Account Number and Holder Name cannot be empty.")
            return #return is used for restart the loop asking for account no and name

        if initial_deposit < 0:
            #checking if initial deposit is negative
            print("Error: Deposit amount cannot be negative.")
            return

        new_account = Account(account_no, holder_name, account_type, initial_deposit)
        #account's information is storing in new_account object by calling Account class that created at the starting of code
        self.accounts[account_no] = new_account
        #new_account object is assigning to self.accounts dictionary with [account_no] key
        print(f"Account for '{holder_name}' created successfully!")
        #output message of inputted account holder's name added successfully

    def view_accounts(self): #function for viewing accounts
        print("\n     Bank Account Records     ")
        if len(self.accounts) == 0:
            #len() is used to check self.accounts{} dictionary is empty or not
            print("No account records found.")
            return #return for back to the loop again
        for account_no in self.accounts: #starting loop if account_no is in self.accounts {} dictionary
            account = self.accounts[account_no] 
            #extracting specific account from self.accounts{} dictionary by using [account_no] key and save it in account object
            print(account.display_info())
             #account object value is entered to display_info() function by dot 

    def search_account(self): #function for searching accounts
        print("\n     Search Account     ")
        account_no = input("Enter Account Number to search: ")
        #taking input of account no for searching account
        if account_no in self.accounts:#starting loop if account_no is in self.accounts {} dictionary
            print("\nAccount Found.")
            print(self.accounts[account_no].display_info())
            #printing account's information using [account_no] key in self.accounts dictionary and entering display_info() function by dot
        else:
            print("Account not found.") #if inputted account_no is not in the dictionary

    def delete_account(self):#function for deleting accounts
        print("\n    Delete Account Record    ")
        account_no = input("Enter Account Number to delete: ")
        if account_no in self.accounts: #starting loop if account_no is in self.accounts {} dictionary
            removed_account = self.accounts.pop(account_no) 
            #entering self.accounts{} dictionary by account_no key to pop/delete by pop() function and store it temporary in removed_account object
            print(f"Account '{removed_account.holder_name}' record deleted successfully.")
            #printing the holder's name by removed_account object entering to holder_name by dot and that was previously stored by dictionary{}
        else:
            print("Account Number not found.") #if inputted account no is not in the dictionary{}


def main(): #the main function that controls the execution of the entire program
    bms = BankManagementSystem() #created an object of the BankManagementSystem class called bms
    while True: #starting the infinite loop until the user exit
        print("\n Welcome to jiban's bank management system")
        print("1. Create new account")
        print("2. View all accounts")
        print("3. Search account by number")
        print("4. Delete account")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == "1":
            bms.add_account()
        elif choice == "2":
            bms.view_accounts()
        elif choice == "3":
            bms.search_account()
        elif choice == "4":
            bms.delete_account()
        elif choice == "5":
            print("\nExiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__": #checking if this script is being run directly as the main program
    main() #calling the main function to start the execution of the program