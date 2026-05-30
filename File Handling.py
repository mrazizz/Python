# accounts = open("accounts.txt", mode="w")
# accounts.write("001 Aziz Rs.10000B\n")
# accounts.write("002 Ahmed Rs.4000\n")
# accounts.write("003 Ali Rs.5000\n")
# accounts.write("004 Aisha Rs.6000\n")
# accounts.close()
# accounts = open("accounts.txt", mode="a")
# accounts.write("005 Amira Rs.7000\n")
# accounts.write("006 Omar Rs.8000\n")
# accounts.close()

# accounts = open("accounts.txt", mode="r")
# print(f"{"IBAN":<10}{"Name":<10}{"Balance":>10}")
# for record in accounts:
#     iban, name, balance = record.split()
#     print(f"{iban:<10}{name:<10}{balance:>10}")
# accounts.close()


id = input("Enter the IBAN to get your balance: ")
accounts = open("accounts.txt", mode="r")
for record in accounts:
    iban, name, balance = record.split()
    if iban == id:
        print(f"IBAN: {iban}\nName: {name}\nBalance: {balance}")
        break
else:
    print("Record not found.")
accounts.close()

# I want to check if file exists or not.
fils = open("acc.txt", mode="a")
fils.close()