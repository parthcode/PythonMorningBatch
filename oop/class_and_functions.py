class StudentDetails:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display(self):
        print(self.name)
        print(self.address)

    def name_value(self):
        return self.name


obj = StudentDetails('Alex', 'Mumbai')  # __init constructor will be called
print(obj.address)
"""
Inheritance
Abstraction
Polymorphism
Encaptulation
"""