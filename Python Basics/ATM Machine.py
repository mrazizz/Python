print("\t----Welcome to the ATM Machine----\n")
Balance = 10000
attempts = 3

def Withdraw(Balance):
    amount = int(input("\tEnter amount in multiples of 1000 to withdraw: "))
    if amount > 50000:
        print("\tAmount exceeds the limit of Rs. 50000")
    elif amount > Balance:
        print("\tInsufficient balance")
    elif amount % 1000 != 0:
        print("\tAmount should be in multiples of Rs. 1000")
    else:
        Balance = Balance - amount
        print(f"\tAmount withdrawn: Rs. {amount}")
        print(f"\tYour balance is: Rs. {Balance}")
    return Balance

def Deposit(Balance):
    amount = int(input("\tEnter amount to deposit: "))
    Balance = Balance + amount
    print(f"\tAmount deposited: Rs. {amount}")
    print(f"\tYour balance is: Rs. {Balance}")
    return Balance

while attempts > 0:
    pin = int(input("\tEnter your 4 digit pin: "))
    if pin != 4719 and attempts > 0:
        print("\tInvalid pin, please try again")
        attempts = attempts - 1
    else:
        break
if attempts == 0:
    print("\tYou have exceeded the maximum number of attempts to enter the correct pin, your card has been blocked.")
    exit()

print("\t----Welcome to your account----\n")
while True:
    print("\t1. Withdraw Amount\n\t2. Deposit Amount\n\t3. Check Balance\n\t4. Exit")
    option = int(input("\tEnter your option: "))
    if option == 1:
        Balance = Withdraw(Balance)
    elif option == 2:
        Balance = Deposit(Balance)
    elif option == 3:
        print(f"\tYour balance is: Rs. {Balance}")
    elif option == 4:
        print("\tThank you for using the ATM Machine")
        exit()
    else:
        print("\tInvalid option, please enter option between 1 and 4")