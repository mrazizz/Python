# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("Number is Even")
# else:
#     print("Number is Odd")

# temp = int(input("Enter temperature in celcius: "))
# if temp > 35:
#     print("It is a hot day")
# else:
#     print("It is a good day")

# temp = int(input("Enter temperature in celcius: "))
# if temp > 35:
#     print("It is a hot day")
# elif temp <= 35 and temp > 10:
#     print("It is sunny day")
# else:
#     print("It is a cold day")

age = int(input("Enter age in years: "))

if age >= 18 and age <=80:
    print("You are eligible for a driving license")
elif age < 18 and age > 0:
    print("You are underage for driving")
elif age > 80:
    print("You are overaged for driving")
else:
    print("Please enter a Valid age")