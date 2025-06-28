class Car:
    def __init__(self, brand, model):
        self.model = model
        # Here we will make brand as private variable
        self.__brand = brand

    def fullName(self):
        return f"Your car is {self.__brand} {self.model}"

    def get_brand(self):
        return f"The Brand Name of your car is: {self.__brand}"


obj1 = Car("Honda", "Civic")
# print(
#     obj1.__brand
# )  Now this will give error because we cant access private variable directly.


# To print brand we would have to use getter
print(obj1.get_brand())
