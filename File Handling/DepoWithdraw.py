file = open("transactions.txt", "w")
file.write("deposit,5000\n")
file.write("withdraw,1000\n")
file.write("deposit,3000\n")
file.write("withdraw,500\n")
file.close()

file = open("transactions.txt", "r")

deposit = 0
withdraw = 0
largest = 0

for line in file:
    type, amount = line.strip().split(",")
    amount = float(amount)

    if type == "deposit":
        deposit += amount
    else:
        withdraw += amount

    if amount > largest:
        largest = amount

file.close()

print("Total Deposits:", deposit)
print("Total Withdrawals:", withdraw)
print("Final Balance:", deposit - withdraw)
print("Largest Transaction:", largest)