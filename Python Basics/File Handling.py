import os

# accounts = open("accounts.txt", mode="w")
# accounts.write("1000 Aziz Rs.10000B\n")
# accounts.write("1001 Ahmed Rs.4000\n")
# accounts.write("1002 Ali Rs.5000\n")
# accounts.write("1003 Aisha Rs.6000\n")
# accounts.close()
# accounts = open("accounts.txt", mode="a")
# accounts.write("1004 Amira Rs.7000\n")
# accounts.write("1005 Omar Rs.8000\n")
# accounts.close()

# accounts = open("accounts.txt", mode="r")
# print(f"{"IBAN":<10}{"Name":<10}{"Balance":>10}")
# for record in accounts:
#     iban, name, balance = record.split()
#     print(f"{iban:<10}{name:<10}{balance:>10}")
# accounts.close()


# id = input("Enter the IBAN to get your balance: ")
# accounts = open("accounts.txt", mode="r")
# for record in accounts:
#     iban, name, balance = record.split()
#     if iban == id:
#         print(f"IBAN: {iban}\nName: {name}\nBalance: {balance}")
#         break
# else:
#     print("Record not found.")
# accounts.close()

print(f"---Welcome to Aziz's Bank Customer Service---")

if os.path.exists("accounts.txt"):
    print("File exists. You can add new accounts.")
else:
    accounts = open("accounts.txt", mode="w")
    accounts.close()
    print("File does not exist. A new file has been created. You can add new accounts.")

while True:
    accounts = open("accounts.txt", mode="r")
    lines = accounts.readlines()
    accounts.close()
    if len(lines) == 0:
        iban = 1000
    else:
        last_line = lines[-1].split()
        last_id = int(last_line[0])
        iban = last_id + 1

    name = input("Enter the account holder's name: ")
    balance = input("Enter the bank balance: ")
    new_record = f"{iban} {name} Rs.{balance}\n"
    accounts = open("accounts.txt", mode="a")
    accounts.write(new_record)

    print("New account added successfully.")
    print(f"Your account details:\nIBAN: {iban}\nName: {name}\nBalance: Rs.{balance}")
    choice = input("Do you want to add another account (Y/n)? ").upper()
    if choice != "Y":
        break
accounts.close()