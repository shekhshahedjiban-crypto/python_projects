#my first calculator program in python

def add(x, y):#function to add two numbers 
    return x + y

def subtract(x, y): #function to subtract two numbers 
    return x - y

def multiply(x, y): #function to multiply two numbers
    return x * y

def divide(x, y): #function to divide two numbers
    if y == 0:
        return "Error!" #division by zero handling
    return x / y

def calculator(): #function to run the calculator program
    # Updated the welcome message to include the author's name
    print("      Jiban's Calculator   ")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True: #if user chooses to exit the calculator,break the loop and exit the programn
        choice = input("\nEnter choice (1/2/3/4/5): ") #prompt user to choose an operation

        if choice == '5': #if user chooses to exit the calculator
            print("Thanks for using Jiban's Calculator. Goodbye!")
            break #if user chooses to exit the calculator,break the loop and exit the program

        if choice in ('1', '2', '3', '4'): #if user choose a valid option,prompt them to enter two numbers and perform the chosen operation
            try: #handle invalid input for numbers
                num1 = float(input("Enter first number: ")) 
                num2 = float(input("Enter second number: "))
            except ValueError: #handle invalid input for numbers
                print("Invalid input. Please enter numbers only.")
                continue #skip the rest of the loop and prompt for input again

            if choice == '1': #if user chooses addition
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2': #if user chooses subtracrtion
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3': #if user chooses multiplication
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4': #if user chooses division
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid Input. Please choose a valid option (1-5).") #if user enters an invalid option,prompt them to choose a valid option

if __name__ == "__main__": #run the calculator function if this script is executed directly
    calculator() #if this script is executed directly,call the calculator function to start the program
