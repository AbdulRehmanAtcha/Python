# while True:
#     try:
#         num1 = int(input("Enter first number: "))
#         num2 = int(input("Enter second number: "))
#         print(f"The sum of {num1} and {num2} is: {num1 + num2}")

#     except Exception as error:
#         print("Error: ", error)
#         break

# Custome error handling
numenator = int(input("Enter numenator: "))
denominator = int(input("Enter denominator: "))

if denominator == 0:
    raise ZeroDivisionError("Cant divide by zero")

print(numenator / denominator)
