import csv

# 1. Create a quick sample CSV file to test with
filename = "data.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Department", "Salary"])  # Headers
    writer.writerow(["Alice", "IT", "75000"])
    writer.writerow(["Bob", "HR", "60000"])
    writer.writerow(["Charlie", "IT", "82000"])

# 2. The Simple Analyzer
print("--- CSV Data Summary ---")
with open(filename, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    
    # Grab the header row first
    headers = next(reader)
    print(f"Columns: {', '.join(headers)}")
    print("-" * 30)
    
    # Loop through the remaining data rows
    row_count = 0
    total_salary = 0
    
    for row in reader:
        print(f"Employee: {row[0]} | Dept: {row[1]} | Salary: ${row[2]}")
        row_count += 1
        total_salary += float(row[2]) # Convert the salary string to a number

print("-" * 30)
print(f"Total Employees: {row_count}")
print(f"Average Salary:  ${total_salary / row_count:.2f}")