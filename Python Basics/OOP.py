class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __str__(self):
        return f"Employee with ID {self.id} is named {self.name}"

emp1 = Employee(1, "Ayan")
emp2 = Employee(2, "Hashir")
emp2.name = "Ali"
emp3 = Employee(3, "Zakir")

print(emp1)
print(emp2)
print(emp3)