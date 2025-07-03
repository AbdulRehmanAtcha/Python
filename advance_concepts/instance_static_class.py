class Employee:

    # Class attribute. Can access from class as well as instance
    company = "HP"

    def __init__(self, name, salary):
        # Instance attribute. Cant access like Employee.name . Have to access like e1.name
        self.name = name
        self.salary = salary

    # Instance method
    def print_info(self):
        return f"Hello, {self.name} with salary: {self.salary}"

    @staticmethod  # A static method is a method inside a class that does not operate on an instance or the class itself. It behaves just like a normal function, but it’s grouped inside a class for logical organization.
    def sum(a, b):
        return a + b

    # Class Method. Can access from class as well as instance
    @classmethod
    def print_company_class(myClass):
        return myClass.company

    @classmethod
    def change_company_class(myClass, newCompany):
        myClass.company = newCompany


e1 = Employee("John Doe", 45000)
# print(e1.print_info())

e2 = Employee("John Doe", 45000)
e2.company = "Google"
# print(e2.company)

# print(e1.sum(2, 3))

print(Employee.print_company_class())
e1.change_company_class("Amazon")
print(Employee.print_company_class())
