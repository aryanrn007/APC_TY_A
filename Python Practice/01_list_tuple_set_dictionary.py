# APL Practical Programs: List, Tuple, Set, Dictionary

# 1. Student Grade Management (List)
names = ["Amit", "Rahul", "Sneha"]
grades = [80, 75, 90]
names.append("Riya")
grades.append(85)
grades[1] = 88
print("Average:", sum(grades) / len(grades))
print("Highest:", max(grades))
print("Lowest:", min(grades))
names.remove("Amit")
grades.pop(0)
print("Students:", names)
print("Grades:", grades)

# 2. Distance between two points (Tuple)
import math
p1 = (2, 3)
p2 = (5, 7)
distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
print("Distance:", distance)

# 3. Server configuration (Tuple and List)
server_ip = (192, 168, 1, 1)
allowed_ips = ["192.168.1.2", "192.168.1.3"]
allowed_ips.append("192.168.1.4")
print("Server IP:", server_ip)
print("Allowed IPs:", allowed_ips)

# 4. Set operations
a = {"Amit", "Rahul", "Sneha"}
b = {"Rahul", "Sneha", "Riya"}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

# 6. Common and unique words in two texts (Set)
a = set(input("Enter first text: ").lower().split())
b = set(input("Enter second text: ").lower().split())
print("Common:", a & b)
print("Only first:", a - b)
print("Only second:", b - a)
print("Total unique:", len(a | b))

# 9. Attendance system (Dictionary and Set)
days = {
    "Monday": {"Amit", "Rahul"},
    "Tuesday": {"Amit", "Sneha"},
    "Wednesday": {"Amit", "Rahul"}
}
all_students = set.union(*days.values())
all_days = set.intersection(*days.values())
print("Unique students:", all_students)
print("Attended every day:", all_days)

# 7. Inventory management (Dictionary)
stock = {"Pen": 10, "Book": 20, "Pencil": 5}
stock["Pen"] = 15
stock["Eraser"] = 8
print("Highest stock:", max(stock, key=stock.get))
print("Total products:", len(stock))
for item in list(stock):
    if stock[item] == 0:
        del stock[item]
print("Inventory:", stock)

# 5. Word frequency (Dictionary)
s = input("Enter a sentence: ").lower()
words = s.split()
frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1
print("Total words:", len(words))
print("Frequency:", frequency)

# 10. Character frequency (Dictionary)
s = input("Enter a string: ").lower()
frequency = {}
for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1
print(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
