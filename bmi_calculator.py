def calculate_bmi(weight_kg, height_m):
    # Formula: weight / (height * height)
    bmi = weight_kg / (height_m ** 2)
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

# --- Example Usage ---
if __name__ == "__main__":
    # Example: 70 kg (154 lbs) and 1.75 meters (5'9")
    weight = 70 
    height = 1.75
    
    bmi_score = calculate_bmi(weight, height)
    category = get_category(bmi_score)
    
    print(f"BMI Score: {bmi_score:.1f}")
    print(f"Category: {category}")