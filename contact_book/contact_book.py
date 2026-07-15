class Contact:
    def __init__(self, contact_id, name, phone, email):
        #function that contain contact id,name,phone,email for object's property
        self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.email = email

    def display_info(self):
        return f"ID: {self.contact_id} | Name: {self.name} | Phone: {self.phone} | Email: {self.email}"
    #function for returning contact's all information in text form


class ContactBookSystem:
    def __init__(self):
        self.contacts = {}  
#function for creating blank dictionary named self.contacts to store contact's information

    def add_contact(self): #function for adding contact
        print("\n    Add New Contact    ")
        contact_id = input("Enter Contact ID: ")
        #checking if the contact id is already exist in the system
        if contact_id in self.contacts:
            print("Error: A contact with this ID already exists.")
            return #for using return loop will be start again for asking contact id input     
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        
        if len(contact_id) == 0 or len(name) == 0 or len(phone) == 0:
            #len() is used for checking the contact id, name or phone is empty or not
            print("Error: ID, Name and Phone cannot be empty.")
            return #return is used for restart the loop asking for inputs
            
        new_contact = Contact(contact_id, name, phone, email)
        #contact's information is storing in new_contact object by caliing Contact class that created at the starting of code
        self.contacts[contact_id] = new_contact
        #new_contact object is assigning to self.contacts dictionary with [contact_id] key
        print(f"Contact '{name}' added successfully!")
        #output message of inputted contact's name added successfully

    def view_contacts(self): #function for viewing contacts
        print("\n     Contact Records     ")
        if len(self.contacts) == 0:
            #len() is used to check self.contacts{} dictionary is empty or not
            print("No contact records found.")
            return #return for back to the loop again
        for contact_id in self.contacts: #starting loop if contact_id is in self.contacts {} dictionary
            contact = self.contacts[contact_id] 
            #extracting specific contact from self.contacts{} dictionary by using [contact_id] key and save it in contact object
            print(contact.display_info())
             #contact object value is entered to display_info() function by dot 

    def search_contact(self): #function for searching contacts
        print("\n     Search Contact     ")
        contact_id = input("Enter Contact ID to search: ")
        #taking input of contact id for searching contact
        if contact_id in self.contacts:#starting loop if contact_id is in self.contacts {} dictionary
            print("\nContact Found.")
            print(self.contacts[contact_id].display_info())
            #printing contact's information using [contact_id] key in self.contacts dictionary and entering display_info() function by dot
        else:
            print("Contact not found.") #if inputted contact_id is not in the dictionary

    def delete_contact(self):#function for deleting contacts
        print("\n    Delete Contact Record    ")
        contact_id = input("Enter Contact ID to delete: ")
        if contact_id in self.contacts: #starting loop if contact_id is in self.contacts {} dictionary
            removed_contact = self.contacts.pop(contact_id) 
            #entering self.contacts{} dictionary by contact_id key to pop/delete by pop() function and store it temporary in removed_contact object
            print(f"Contact '{removed_contact.name}' record deleted successfully.")
            #printing the contact's name by removed_contact object entering to name by dot and that was previously stored by dictionary{}
        else:
            print("Contact ID not found.") #if inputted contact id is not in the dictionary{}


def main(): #the main function that controls the execution of the entire program
    cbs = ContactBookSystem() #created an object of the ContactBookSystem class called cbs
    while True: #starting the infite loop untill the user exit
        print("\n Welcome to jiban's contact book system")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contact by id")
        print("4. Delete contact")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == "1":
            cbs.add_contact()
        elif choice == "2":
            cbs.view_contacts()
        elif choice == "3":
            cbs.search_contact()
        elif choice == "4":
            cbs.delete_contact()
        elif choice == "5":
            print("\nExiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__": #checking if this script is being run directly as the main program
    main() #calling the main function to start the execution of the program
