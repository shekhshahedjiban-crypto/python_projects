class Student:
    def __init__(self, student_id, name, age, grade):
        #function that contain student id,name,age,grade for object's property
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self): 
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Grade: {self.grade}"
    #function for returning student's all information in text form


class StudentManagementSystem:
    def __init__(self):
        self.students = {}  
#function for creating blank dictionary named self.students to store student's information
    def add_student(self): #function for adding student
        print("\n    Add New Student    ")
        student_id = input("Enter Student ID: ")
        #checking if the student id is already exist in the system
        if student_id in self.students:
            print("Error: A student with this ID already exists.")
            return #for using return loop will be start again for asking student id input     
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        grade = input("Enter Grade/Class: ")
        if len(student_id) == 0 or len(name) == 0:
            #len() is used for checking the student id or name is empty or not
            print("Error: ID and Name cannot be empty.")
            return #return is used for restart the loop asking for student id and name
        new_student = Student(student_id, name, age, grade)
        #student's information is storing in new_student object by caliing Student class that created at the starting of code
        self.students[student_id] = new_student
        #new_student object is assigning to self.students dictionary with [student_id] key
        print(f"Student '{name}' added successfully!")
        #output message of inputted student's name added successfully

    def view_students(self): #function for viewing students
        print("\n     Student Records    ")
        if len(self.students) == 0:
            #len() is used to check self.students{} dictionary is empty or not
            print("No student records found.")
            return #return for back to the loop again
        for student_id in self.students: #starting loop if student_id is in self.students {} dictionary
            student = self.students[student_id] 
            #extracting specific student from self.students{} dictionary by using [student_id] key and save it in student object
            print(student.display_info())
             #student object value is entered to display_info() function by dot 

    def search_student(self): #function for searching students
        print("\n     Search Student     ")
        student_id = input("Enter Student ID to search: ")
        #taking input of student id for searching student
        if student_id in self.students:#starting loop if student_id is in self.students {} dictionary
            print("\nStudent Found.")
            print(self.students[student_id].display_info())
            #printing student's information using [studen_id] key in self.students dictionary and entering display_info() function by dot
        else:
            print("Student not found.") #if inputted student_id is not in the dictionary

    def delete_student(self):#function for deleting students
        print("\n    Delete Student Record    ")
        student_id = input("Enter Student ID to delete: ")
        if student_id in self.students: #starting loop if student_id is in self.students {} dictionary
            removed_student = self.students.pop(student_id) 
            #entering self.students{} dictionary by student_id key to pop/delete by pop() function and store it temporary in removed_student object
            print(f"Student '{removed_student.name}' record deleted successfully.")
            #printing the student's name by removed_name object entering to name by dot and that was previously stored by dictionary{}
        else:
            print("Student ID not found.") #if inputted student id is not in the dictionary{}


def main(): #the main function that controls the execution of the entire program
    sms = StudentManagementSystem() #created an object of the StudentManagementSystem class called sms
    while True: #starting the infite loop untill the user exit
        print("\n Welcome to jiban's student management system")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by id")
        print("4. Delete student")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == "1":
            sms.add_student()
        elif choice == "2":
            sms.view_students()
        elif choice == "3":
            sms.search_student()
        elif choice == "4":
            sms.delete_student()
        elif choice == "5":
            print("\nExiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 5.")

if __name__ == "__main__": #checking if this script is being run directly as the main program
    main() #calling the main function to start the execution of the program