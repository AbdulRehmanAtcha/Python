# try:
#     a = 34 / 10
#     print(a)


# except:
#     print("Cant divide by 0")


# This will execute when try block executes
# else:
#     print("Hello World")


try:
    a = 34 / 0
    print(a)


except:
    print("Cant divide by 0")


# This will always executed
finally:
    print("Finally !Hello World")
