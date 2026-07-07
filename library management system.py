class Library:
    def __init__(self):
        # Dictionary stores book_id: {"title": title, "author": author, "borrower": None}
        self.books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print(f"Error: Book ID {book_id} already exists.")
            return
        self.books[book_id] = {"title": title, "author": author, "borrower": None}
        print(f"Book '{title}' added successfully.")

    def borrow_book(self, book_id, member_name):
        if book_id not in self.books:
            print("Error: Book not found.")
            return
        
        book = self.books[book_id]
        if book["borrower"] is not None:
            print(f"Error: '{book['title']}' is already borrowed by {book['borrower']}.")
            return

        book["borrower"] = member_name
        print(f"Success: {member_name} borrowed '{book['title']}'.")

    def return_book(self, book_id):
        if book_id not in self.books:
            print("Error: Book not found.")
            return
        
        book = self.books[book_id]
        if book["borrower"] is None:
            print(f"Error: '{book['title']}' was not borrowed.")
            return

        print(f"Success: '{book['title']}' returned by {book['borrower']}.")
        book["borrower"] = None

    def display_books(self):
        print("\n--- Library Catalog ---")
        if not self.books:
            print("No books available.")
            return
            
        for b_id, info in self.books.items():
            status = f"Borrowed by {info['borrower']}" if info["borrower"] else "Available"
            print(f"ID: {b_id} | '{info['title']}' by {info['author']} [{status}]")


def main():
    library = Library()
    
    # Pre-populate sample books to test instantly
    library.add_book("101", "The Hobbit", "J.R.R. Tolkien")
    library.add_book("102", "1984", "George Orwell")

    while True:
        print("\n=== LIBRARY SYSTEM ===")
        print("1. Add Book\n2. Borrow Book\n3. Return Book\n4. View Books\n5. Exit")
        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            b_id = input("Enter Book ID: ").strip()
            title = input("Enter Title: ").strip()
            author = input("Enter Author: ").strip()
            if b_id and title and author:
                library.add_book(b_id, title, author)
        
        elif choice == "2":
            b_id = input("Enter Book ID to borrow: ").strip()
            name = input("Enter Your Name: ").strip()
            if b_id and name:
                library.borrow_book(b_id, name)
                
        elif choice == "3":
            b_id = input("Enter Book ID to return: ").strip()
            if b_id:
                library.return_book(b_id)
                
        elif choice == "4":
            library.display_books()
            
        elif choice == "5":
            print("\nExiting system. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()