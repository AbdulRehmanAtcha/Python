#


a = int(input("Enter number: "))
# table = []
# for i in range(1, 11):
#     table.append(a * i)

# print(table)


# Short cut for the above code is list comprehension
table = [a * i for i in range(1, 11)]
print(table)
