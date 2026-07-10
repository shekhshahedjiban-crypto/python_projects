def calculate_bmi(weight, height):
    #formula of bmi= weight/height(m)^2
    bmi = weight / (height ** 2)
    return bmi 

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    print("Welcome to Jiban's BMI Calculator")
    
    #taking input from the user and convert to decimal numbers (floats)
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    
    # 2. Run the functions with the user inputs
    bmi_score = calculate_bmi(weight, height)
    category = get_category(bmi_score)
    
    #(.1f) is uesd to give the output in single float number
    print(f"\nBMI Score: {bmi_score:.1f}") 
    print(f"Category: {category}")