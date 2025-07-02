class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        pass

    # Getter
    # def first_name(self):
    #     return self.name.split(" ")[0]

    # Setter
    # def change_first_name(self, newFirstName):
    #     oldName = self.name.split(" ")
    #     new_name = f"{newFirstName} {oldName[1]}"
    #     return new_name

    # There is a thing called property decorator. This means we have created function as propert(Variable)
    @property
    def first_name(self):
        return self.name.split(" ")[0]

    # There is another thing called property setter
    @first_name.setter
    def first_name(self, newFirstName):
        oldName = self.name.split(" ")
        newName = f"{newFirstName} {oldName[1]}"
        self.name = newName


e1 = Employee("John Doe", 3333)
# print(e1.name)
# print(e1.change_first_name(newFirstName="Jack"))

# We are calling property. Look no () as we typically do in function calling
print(e1.first_name)
e1.first_name = "Jack"
print(e1.name)
