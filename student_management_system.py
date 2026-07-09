class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Grade: {self.grade}"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}  # Dictionary to store students using ID as the key

    def add_student(self):
        print("\n--- Add New Student ---")
        student_id = input("Enter Student ID: ").strip()
        
        if student_id in self.students:
            print("Error: A student with this ID already exists.")
            return
            
        name = input("Enter Name: ").strip()
        age = input("Enter Age: ").strip()
        grade = input("Enter Grade/Class: ").strip()
        
        if not student_id or not name:
            print("Error: ID and Name cannot be empty.")
            return

        # Create student object and add to dictionary
        new_student = Student(student_id, name, age, grade)
        self.students[student_id] = new_student
        print(f"Student '{name}' added successfully!")

    def view_students(self):
        print("\n--- Student Records ---")
        if not self.students:
            print("No student records found.")
            return
            
        for student in self.students.values():
            print(student.display_info())

    def search_student(self):
        print("\n--- Search Student ---")
        student_id = input("Enter Student ID to search: ").strip()
        
        if student_id in self.students:
            print("\nStudent Found:")
            print(self.students[student_id].display_info())
        else:
            print("Student not found.")

    def delete_student(self):
        print("\n--- Delete Student Record ---")
        student_id = input("Enter Student ID to delete: ").strip()
        
        if student_id in self.students:
            removed_student = self.students.pop(student_id)
            print(f"Student '{removed_student.name}' record deleted successfully.")
        else:
            print("Student ID not found.")


def main():
    sms = StudentManagementSystem()
    
    while True:
        print("\n=== STUDENT MANAGEMENT SYSTEM ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ").strip()
        
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

if __name__ == "__main__":
    main()