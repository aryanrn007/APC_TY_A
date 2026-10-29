try:
    name = input("Enter Employee Name:")
    roll_no = int(input("Enter Employee ID:"))
    salary = float(input("Enter Salary:"))

    if salary < 0 or salary > 100000:
        raise ValueError("Salary should be between 0 and 100000.")

    print("\nEmployee Record:")
    print("Name:", name)
    print("Employee ID:", roll_no)
    print("Salary:", salary)

except ValueError as e:
    print("Error:", e)

finally:
    print("Program completed.")