import numpy as np

marks = np.array([78, 85, 92, 67, 88, 74, 95, 81, 69, 90,
                  72, 84, 91, 63, 87, 76, 89, 70, 94, 80])
average = np.mean(marks)
print("Class average:", average)
print("Marks above average:", marks[marks > average])
