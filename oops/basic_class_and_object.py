class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"Your car is {self.brand} {self.model}"


# self. means variables of class.
# (brand,model) are parameters

# Instance
obj1 = Car("Toyota", "Civic")
print(obj1.fullName())

obj2 = Car("Kia", "Sportage")
print(obj2.fullName())
