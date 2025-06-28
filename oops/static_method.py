class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullName(self):
        return f"Your car is {self.brand} {self.model}"

    @staticmethod  # Decorators
    def general_description():
        return "Cars are meant for transport"


obj1 = Car("Kia", "Sportage")
print(Car.general_description())
