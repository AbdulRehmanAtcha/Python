# def something():
#     print("Something...")
#     print("Something...")
#     print("Something...")
#     print("Something...")
#     print("Something...")

#     return 5


# a = something()
# if a > 4:
# print(a)


# if (a := something()) > 4:
#     print("Hello")
# else:
#     print("Noi")


# This walrus operator is for assigning and checking in a single line
while data := input("Enter anything: "):
    if data.lower() == "q" or data.lower() == "quit":
        break
    print(data)
