class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Success: ${amount:.2f} deposited.")
            self.check_balance()
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Error: Insufficient funds. Available balance: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Success: ${amount:.2f} withdrawn.")
            self.check_balance()

    def check_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.balance:.2f}")


def main():
    print("--- Welcome to the Bank Account System ---")
    name = input("Enter your name to create an account: ").strip()
    
    # Initialize an account with a starting balance of $100.00
    user_account = BankAccount(account_number="123456", account_holder=name, initial_balance=100.0)
    print(f"\nWelcome {name}! Your account has been created with a $100.00 bonus.")

    while True:
        print("\n=== BANK MENU ===")
        print("1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
        choice = input("\nChoose an option (1-4): ").strip()

        if choice == "1":
            print()
            user_account.check_balance()
            
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: $"))
                user_account.deposit(amount)
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: $"))
                user_account.withdraw(amount)
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == "4":
            print("\nThank you for banking with us. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()