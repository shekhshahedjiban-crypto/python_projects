def km_to_miles(km): # Function to convert kilometers to miles
    return km * 0.621371 #converting km to miles using the conversion factor

def celsius_to_fahrenheit(celsius):# Function to convert Celsius to Fahrenheit
    return (celsius * 9/5) + 32 #covertion formula for celcius to fahrenheit 

if __name__ == "__main__":
    print("  Jiban's Unit Converter  ")
    print("1. Convert Kilometers to Miles")
    print("2. Convert Celsius to Fahrenheit")
   
    
    # taking user input for the choice of conversion
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == "1": 
        try: #try block is used for handling input errors like value errors when the user enters a non numeric value for kilometers or celcius
            #taking Kilometers input from the user
            km_value = float(input("Enter distance in kilometers: "))
            miles_result = km_to_miles(km_value)
            print(f" {km_value} km is equal to {miles_result} miles")
        except ValueError: #if a value error occurs,the except block will be executed and will give error message 
            print(" Invalid input! Please enter a valid number for kilometers.")
            
    elif choice == "2":
        try:
            #taking Celsius input from the user
            c_value = float(input("Enter temperature in Celsius: "))
            f_result = celsius_to_fahrenheit(c_value)
            print(f" {c_value}°C is equal to {f_result}°F")
        except ValueError:
            print(" Invalid input! Please enter a valid number for temperature.")
            
    else:
        print(" Invalid choice! Please restart and select 1 or 2.")
