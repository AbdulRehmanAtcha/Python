# Polymorphism means same methods can be of different type depends upon how they are used
class Car:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name

    def full_name(self):
        return f"Your car is {self.brand} {self.name}"

    # Polymorphism
    def fuel_type(self):
        return "Petrol or diesel"


class ElectricCar(Car):
    def __init__(self, brand, name, battery_size):
        self.batter_size = battery_size
        super().__init__(brand, name)

    # Polymorphism
    def fuel_type(self):
        return "Electric charge"


obj1 = Car("Tesla", "S Model")
obj2 = ElectricCar("Tesla", "S Model", "85Kwh")
# print(obj1.full_name(), "with battery size", obj1.batter_size)
print(obj1.fuel_type())
print(obj2.fuel_type())
