# class Employee:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name
#     def __str__(self):
#         return f"Employee with ID {self.id} is named {self.name}"

# emp1 = Employee(1, "Ayan")
# emp2 = Employee(2, "Hashir")
# emp2.name = "Ali"
# emp3 = Employee(3, "Zakir")

# print(emp1)
# print(emp2)
# print(emp3)


# Inheritance
# class Animal:
#     def eat(self):
#         print("I can eat")
#     def sleep(self):
#         print("I can sleep")

# class Dog(Animal):
#     def bark(self):
#         print("I can bark woof woof")

# dog1 = Dog()
# dog1.eat()
# dog1.sleep()
# dog1.bark()

# class Computer:
#     def __init__(self):
#         self.__maxprice = 799
#     def sell(self):
#         print(f"Selling Price: {self.__maxprice}")
#     def setMaxPrice(self, price):
#         self.__maxprice = price

# comp = Computer()
# comp.sell()
# comp.setMaxPrice(1199)
# comp.sell()

class Car:
    def __init__(self, model):
        self.model = model
    def start(self):
        print(f"{self.model} has started.")

car1 = Car("Toyota")
car1.start()