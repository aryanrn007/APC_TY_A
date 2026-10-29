import numpy as np

arr = np.array([12, 67, 45, 89, 50, 72, 31, 99, 4, 56])
arr[arr > 50] = 0
print("Updated array:", arr)
