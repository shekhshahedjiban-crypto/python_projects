import csv  # importing built-in csv module to write, read and analyze csv files

class Employee:
    def __init__(self, name, department, salary):
        #function that contain name,department,salary for object's property
        self.name = name
        self.department = department
        self.salary = float(salary)  # converting salary string to float for mathematical calculation

    def display_info(self):
        return f"Employee: {self.name} | Dept: {self.department} | Salary: ${self.salary:.2f}"
    #function for returning employee's all information in text form


class SimpleCSVAnalyzerSystem:
    def __init__(self):
        self.employees = {}  
#function for creating blank dictionary named self.employees to store data from csv file
        self.filename = "data.csv"  # string to store the target csv file name as a property

    def create_sample_csv(self): #function for creating a quick sample CSV file to test with
        # opening the file in write mode ('w') with utf-8 encoding to prevent formatting issues
        with open(self.filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file) # creating a writer object to write rows into the csv file
            # writing headers into csv file using writerow() function
            writer.writerow(["Name", "Department", "Salary"])  
            # adding raw data row 1 with JIBAN inside the created data.csv file
            writer.writerow(["JIBAN", "IT", "75000"]) 
            # adding raw data row 2 with HASNAT inside the created data.csv file
            writer.writerow(["HASNAT", "HR", "60000"])   
            # adding raw data row 3 with LABIB inside the created data.csv file
            writer.writerow(["LABIB", "IT", "82000"]) 
        print(f"Sample file '{self.filename}' created successfully for testing!")
        # output message showing that the csv file was successfully created on hard disk

    def load_and_analyze_data(self): #function for reading, parsing and analyzing csv data
        print("\n--- CSV Data Summary ---")
        
        try:
            # opening the created csv file in read mode ('r') to access data rows
            with open(self.filename, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file) # creating a reader object to read and parse the csv data
                
                # grab the very first line as headers using next() function
                headers = next(reader)
                print(f"Columns: {', '.join(headers)}") # formatting and printing column names
                print("-" * 45) # printing table design separator lines
                
                self.employees = {} # resetting dictionary before loading fresh data from file
                row_count = 0 # initializing counter variable with 0 to count total rows/employees
                total_salary = 0.0 # initializing total_salary with 0.0 value to calculate average salary
                
                #loop through the remaining data rows of the csv file after headers
                for row in reader:
                    if row: # checking if the row is not empty to avoid system crash
                        name = row[0]        # extracting employee name from index 0 of the row list
                        department = row[1]  # extracting department from index 1 of the row list
                        salary = row[2]      # extracting salary string from index 2 of the row list
                        
                        # creating an object of Employee class and storing information as properties
                        emp_object = Employee(name, department, salary)
                        
                        # saving the object into self.employees dictionary using name as unique key
                        self.employees[name] = emp_object
                        
                        # printing employee information details using display_info() function by dot
                        print(emp_object.display_info())
                        
                        row_count += 1 # incrementing row counter in every loop execution
                        total_salary += emp_object.salary # adding current employee salary to total_salary variable
                
                if row_count == 0: # checking if the csv file has no data rows inside it
                    print("No employee data found in CSV.")
                    return # return for back to the main loop menu again

                print("-" * 45) # printing table design separator lines
                print(f"Total Employees: {row_count}") # printing final calculated total row count
                print(f"Average Salary:  ${total_salary / row_count:.2f}") # printing calculated average salary value
                
        except FileNotFoundError:
            # showing error message if data.csv file does not exist in the folder path
            print(f"Error: '{self.filename}' file not found. Please run Option 1 first.")


def main(): #the main function that controls the execution of the entire program
    scas = SimpleCSVAnalyzerSystem() #created an object of the SimpleCSVAnalyzerSystem class called scas
    
    while True: #starting the infinite loop until the user exit
        print("\n Welcome to jiban's Simple CSV Analyzer")
        print("1. Create Sample CSV File")
        print("2. Load and Analyze CSV Data")
        print("3. Exit")
        
        choice = input("\nChoose an option (1-3): ").strip()
        #taking input from user to choose a menu option between 1 to 3
        
        if choice == "1":
            scas.create_sample_csv() # calling create_sample_csv() function from scas object if choice is 1
        elif choice == "2":
            scas.load_and_analyze_data() # calling load_and_analyze_data() function from scas object if choice is 2
        elif choice == "3":
            print("\nExiting Analyzer. Goodbye!")
            break # breaking the infinite while loop to close the program execution
        else:
            print("Invalid choice! Please select a number between 1 and 3.")
            #printing error message if choice input is anything else outside 1 to 3

if __name__ == "__main__": #checking if this script is being run directly as the main program
    main() #calling the main function to start the execution of the program
