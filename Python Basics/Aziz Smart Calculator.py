import math
print("\t***Welcome to Aziz's Smart Calculator***\t")

def add():
    num1 = int(input("\tEnter Number 1: "))
    num2 = int(input("\tEnter Number 2: "))
    print(f"\t{num1} + {num2} = {num1 + num2}")
def subtract():
    num1 = int(input("\tEnter Number 1: "))
    num2 = int(input("\tEnter Number 2: "))
    print(f"\t{num1} - {num2} = {num1 - num2}")
def multiply():
    num1 = int(input("\tEnter Number 1: "))
    num2 = int(input("\tEnter Number 2: "))
    print(f"\t{num1} x {num2} = {num1 * num2}")
def divide():
    num1 = int(input("\tEnter Number 1: "))
    num2 = int(input("\tEnter Number 2: "))
    print(f"\t{num1} / {num2} = {num1 / num2}")
def sin():
    angle = int(input("\tEnter Angle in Degrees: "))
    print(f"\tsin({angle}) = {math.sin(angle)}")
def cos():
    angle = int(input("\tEnter Angle in Degrees: "))
    print(f"\tcos({angle}) = {math.cos(angle)}")
def tan():
    angle = int(input("\tEnter Angle in Degrees: "))
    print(f"\ttan({angle}) = {math.tan(angle)}")
    
while True:
    choice = int(input("\tWhat Operation do you want to perfrom?\n\t1. Arithmetic Operations.\n\t2. Trignometric Operations.\n\t3. Exit\n\tEnter your choice: "))
    if choice == 1:
        print("\tWhat operation you want to perfrom?\n\t1. Additon\n\t2. Subtraciton\n\t3. Multiplication\n\t4. Divison")
        arithmetic_choice = int(input("\tEnter you choice: "))
        if arithmetic_choice == 1:
            add()
        elif arithmetic_choice == 2:
            subtract()
        elif arithmetic_choice == 3:
            multiply()
        elif arithmetic_choice == 4:
            divide()
        else:
            print("\tEnter a valid choice.")
    elif choice == 2:
        print("\tWhat operation you want to perfrom?\n\t1. Sin\n\t2. Cos\n\t3. Tan")
        trig_choice = int(input("\tEnter you choice: "))
        if trig_choice == 1:
            sin()
        elif trig_choice == 2:
            cos()
        elif trig_choice == 3:
            tan()
        else:
            print("\tEnter a valid choice.")
    elif choice == 3:
        print("\tThank you for using Aziz's Smart Calculator")
        exit()
    else:
        print("\tEnter a valid choice.")