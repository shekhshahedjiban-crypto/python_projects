class ContactBook:
    def __init__(self):
        # Dictionary stores name: {"phone": phone, "email": email}
        self.contacts = {}

    def add_contact(self, name, phone, email):
        if name.lower() in [k.lower() for k in self.contacts]:
            print(f"Error: A contact named '{name}' already exists.")
            return
        self.contacts[name] = {"phone": phone, "email": email}
        print(f"Success: Contact '{name}' added.")

    def view_contacts(self):
        print("\n--- Contact List ---")
        if not self.contacts:
            print("Your contact book is empty.")
            return
        
        for name, info in sorted(self.contacts.items()):
            print(f"Name: {name} | Phone: {info['phone']} | Email: {info['email']}")

    def search_contact(self, name):
        print("\n--- Search Result ---")
        # Case-insensitive search match
        for key in self.contacts:
            if key.lower() == name.lower():
                print(f"Found: {key} | Phone: {self.contacts[key]['phone']} | Email: {self.contacts[key]['email']}")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for key in list(self.contacts.keys()):
            if key.lower() == name.lower():
                del self.contacts[key]
                print(f"Success: Contact '{key}' has been deleted.")
                return
        print(f"Error: Contact '{name}' not found.")


def main():
    book = ContactBook()
    
    # Pre-populate sample contacts for instant testing
    book.add_contact("Alice Smith", "123-456-7890", "alice@email.com")
    book.add_contact("Bob Jones", "987-654-3210", "bob@email.com")

    while True:
        print("\n=== CONTACT BOOK ===")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            name = input("Enter Name: ").strip()
            phone = input("Enter Phone Number: ").strip()
            email = input("Enter Email Address: ").strip()
            if name and phone:
                book.add_contact(name, phone, email)
            else:
                print("Error: Name and Phone number are required.")
                
        elif choice == "2":
            book.view_contacts()
            
        elif choice == "3":
            name = input("Enter Name to search: ").strip()
            if name:
                book.search_contact(name)
                
        elif choice == "4":
            name = input("Enter Name to delete: ").strip()
            if name:
                book.delete_contact(name)
                
        elif choice == "5":
            print("\nExiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()