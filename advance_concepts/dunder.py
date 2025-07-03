class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.name} {self.salary}"

    def __len__(self):
        lenth = len(self.name)
        return lenth + 1
        # return int(f"{len(self.name)} + {1}")


e1 = Employee("Jack", 30000)
print(str(e1))
print(len(e1))
