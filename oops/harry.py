# class Employee:
#     company = "Google"

#     def get_salary(self):
#         return 34000


# e1 = Employee()
# print(e1.get_salary())


# Constructors
# class Employee:
#     company = "Google"

#     def __init__(self, salary, name, bond):
#         self.salary = salary
#         self.name = name
#         self.bond = bond

#     def get_salary(self):
#         return self.salary

#     def get_info(self):
#         return (
#             f"Employee: {self.name}'s salary is: {self.salary} and bond is: {self.bond}"
#         )


# e1 = Employee(34000, "Abdul Rehman", 3)
# print(e1.get_info())


# Instance and class attribute
class Employee:
    company = "Google"

    def __init__(self, salary, name, bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary

    def get_info(self):
        return f"Company: {self.company}. Employee: {self.name}'s salary is: {self.salary} and bond is: {self.bond}"


e1 = Employee(34000, "Abdul Rehman", 3, "Amazon")
print(e1.get_info())
