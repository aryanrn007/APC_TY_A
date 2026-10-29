file = open("attendance.txt", "w")
file.write("101,Amit,80,100\n")
file.write("102,Priya,70,100\n")
file.write("103,Rahul,90,100\n")
file.close()

file = open("attendance.txt", "r")

for line in file:
    roll, name, present, total = line.strip().split(",")
    percentage = int(present) / int(total) * 100
    print(name, percentage, "%")
    
    if percentage < 75:
        print("Below 75%:", name)

file.close()