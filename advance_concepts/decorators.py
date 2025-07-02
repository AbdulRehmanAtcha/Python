# A decorator is a function that takes another function as an argument. Inside the decorator, there is usually a nested (inner) function that can call the original function (the one passed as an argument), possibly adding some extra behavior before or after it. In the end, the decorator returns this inner function.


def myDecorator(func):
    def wrapper():
        print("Print Loading")
        func()
        print("Printed successfully!")

    return wrapper


@myDecorator
def greet_user():
    print("Hello, user!")


# my_func = decorator(greet_user)
# my_func()
greet_user()
