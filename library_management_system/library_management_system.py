class Book:
    def __init__(self, book_id, title, author):
        #function that contain book id,title,author,borrower for object's property
        self.book_id = book_id
        self.title = title
        self.author = author
        self.borrower = None
        #assigning None to borrower property because new book is not borrowed by anyone yet

    def display_info(self):
        status = f"Borrowed by {self.borrower}" if self.borrower else "Available"
        return f"ID: {self.book_id} | '{self.title}' by {self.author} [{status}]"
    #function for returning book's all information in text form


class LibraryManagementSystem:
    def __init__(self):
        self.books = {}  
#function for creating blank dictionary named self.books to store book's information

    def add_book(self): #function for adding book
        print("\n    Add New Book    ")
        book_id = input("Enter Book ID: ")
        #checking if the book id is already exist in the system
        if book_id in self.books:
            print(f"Error: Book ID {book_id} already exists.")
            return #for using return loop will be start again for asking book id input     
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        if len(book_id) == 0 or len(title) == 0 or len(author) == 0:
            #len() is used for checking the book id, title or author is empty or not
            print("Error: ID, Title and Author cannot be empty.")
            return #return is used for restart the loop asking for book id and title
        new_book = Book(book_id, title, author)
        #book's information is storing in new_book object by calling Book class that created at the starting of code
        self.books[book_id] = new_book
        #new_book object is assigning to self.books dictionary with [book_id] key
        print(f"Book '{title}' added successfully!")
        #output message of inputted book's title added successfully

    def borrow_book(self): #function for borrowing book
        print("\n    Borrow Book    ")
        book_id = input("Enter Book ID to borrow: ")
        if book_id not in self.books:
            print("Error: Book not found.")
            return
        
        book = self.books[book_id]
        #extracting specific book from self.books{} dictionary by using [book_id] key and save it in book object
        if book.borrower is not None:
            print(f"Error: '{book.title}' is already borrowed by {book.borrower}.")
            return

        member_name = input("Enter Your Name: ")
        if len(member_name) == 0:
            print("Error: Borrower name cannot be empty.")
            return

        book.borrower = member_name
        print(f"Success: {member_name} borrowed '{book.title}'.")

    def return_book(self): #function for returning book
        print("\n    Return Book    ")
        book_id = input("Enter Book ID to return: ")
        if book_id not in self.books:
            print("Error: Book not found.")
            return
        
        book = self.books[book_id]
        #extracting specific book from self.books{} dictionary by using [book_id] key and save it in book object
        if book.borrower is None:
            print(f"Error: '{book.title}' was not borrowed.")
            return

        print(f"Success: '{book.title}' returned by {book.borrower}.")
        book.borrower = None

    def view_books(self): #function for viewing books
        print("\n     Library Catalog     ")
        if len(self.books) == 0:
            #len() is used to check self.books{} dictionary is empty or not
            print("No books available.")
            return #return for back to the loop again
        for book_id in self.books: #starting loop if book_id is in self.books {} dictionary
            book = self.books[book_id] 
            #extracting specific book from self.books{} dictionary by using [book_id] key and save it in book object
            print(book.display_info())
             #book object value is entered to display_info() function by dot 


def main(): #the main function that controls the execution of the entire program
    lms = LibraryManagementSystem() #created an object of the LibraryManagementSystem class called lms
    while True: #starting the infinite loop until the user exit
        print("\n Welcome to jiban's library management system")
        print("1. Add book")
        print("2. Borrow book")
        print("3. Return book")
        print("4. View all books")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == "1":
            lms.add_book()
        elif choice == "2":
            lms.borrow_book()
        elif choice == "3":
            lms.return_book()
        elif choice == "4":
            lms.view_books()
        elif choice == "5":
            print("\nExiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__":  #checking if this script is being run directly as the main program
    main() #calling the main function to start the execution of the program.
