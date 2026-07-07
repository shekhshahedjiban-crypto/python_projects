from datetime import datetime

class ExpenseTracker:
    def __init__(self, budget=0.0):
        self.budget = budget
        # List of dicts: [{"date": str, "category": str, "amount": float, "description": str}]
        self.expenses = []

    def add_expense(self, category, amount, description):
        if amount <= 0:
            print("Error: Expense amount must be greater than zero.")
            return
            
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
        expense = {
            "date": date_str,
            "category": category,
            "amount": amount,
            "description": description
        }
        self.expenses.append(expense)
        print(f"Success: Added ${amount:.2f} under '{category}'.")

    def get_total_spent(self):
        return sum(item["amount"] for item in self.expenses)

    def display_summary(self):
        print("\n--- EXPENSE REPORT ---")
        if not self.expenses:
            print("No expenses recorded yet.")
            return

        print(f"{'Date':<17} | {'Category':<12} | {'Amount':<10} | {'Description'}")
        print("-" * 60)
        for item in self.expenses:
            print(f"{item['date']} | {item['category']:<12} | ${item['amount']:<9.2f} | {item['description']}")
        
        total_spent = self.get_total_spent()
        print("-" * 60)
        print(f"Total Amount Spent: ${total_spent:.2f}")
        
        if self.budget > 0:
            remaining = self.budget - total_spent
            print(f"Remaining Budget:   ${remaining:.2f}")
            if remaining < 0:
                print(" Warning: You have exceeded your budget!")


def main():
    print("--- Welcome to Personal Expense Tracker ---")
    try:
        budget_input = input("Enter your monthly budget limit (or press Enter for no limit): ").strip()
        budget = float(budget_input) if budget_input else 0.0
    except ValueError:
        print("Invalid input. Starting with no budget limit.")
        budget = 0.0

    tracker = ExpenseTracker(budget)

    while True:
        print("\n=== EXPENSE TRACKER MENU ===")
        print("1. Add Expense\n2. View Summary Report\n3. Exit")
        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            category = input("Enter category (e.g., Food, Rent, Transport): ").strip()
            description = input("Enter description/notes: ").strip()
            try:
                amount = float(input("Enter amount spent: $"))
                if category and amount:
                    tracker.add_expense(category, amount, description)
                else:
                    print("Error: Category and Amount are required fields.")
            except ValueError:
                print("Error: Please enter a valid number for the amount.")
                
        elif choice == "2":
            tracker.display_summary()
            
        elif choice == "3":
            print("\nExiting Tracker. Stay on top of your financial goals!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 3.")

if __name__ == "__main__":
    main()