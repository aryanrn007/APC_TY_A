try:
    name = input("Enter Student Name:")
    roll_no = int(input("Enter roll number:"))
    marks = float(input("Enter marks:"))

    if marks < 0 or marks > 100:
        raise ValueError("Marks should be between 0 and 100.")

    print("\nStudent Record:")
    print("Name:", name)
    print("Roll Number:", roll_no)
    print("Marks:", marks)

except ValueError as e:
    print("Error:", e)

finally:
    print("Program completed.")