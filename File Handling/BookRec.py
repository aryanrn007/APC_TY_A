def add_book():
    id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")

    file = open("books.txt", "a")
    file.write(id + "," + title + "," + author + ",Available\n")
    file.close()

def search_book():
    id = input("Enter book ID: ")
    file = open("books.txt", "r")

    for line in file:
        data = line.strip().split(",")
        if data[0] == id:
            print(line.strip())

    file.close()

def issue_book():
    id = input("Enter book ID: ")
    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("books.txt", "w")
    for line in lines:
        data = line.strip().split(",")
        if data[0] == id and data[3] == "Available":
            data[3] = "Issued"
        file.write(",".join(data) + "\n")
    file.close()

def return_book():
    id = input("Enter book ID: ")
    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("books.txt", "w")
    for line in lines:
        data = line.strip().split(",")
        if data[0] == id:
            data[3] = "Available"
        file.write(",".join(data) + "\n")
    file.close()

def display_available():
    file = open("books.txt", "r")
    for line in file:
        if "Available" in line:
            print(line.strip())
    file.close()

add_book()
search_book()
issue_book()
return_book()
display_available()