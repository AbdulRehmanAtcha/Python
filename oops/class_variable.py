class Car:
    # Class variable means its shared across all instances
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    def fullName(self):
        return f"Your car is {self.brand} {self.model}"


obj1 = Car("Kia", "Sportage")
obj2 = Car("Kia", "Stonic")
obj3 = Car("Kia", "Stonic")
print(Car.total_cars)
