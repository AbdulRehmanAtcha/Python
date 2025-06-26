# Lists can have multiple data types
# Lists are mutable

marks = [89, 80, 95, 90, 92, 23]
mixed = ["Helol", 1, "World", 0, True]


# Lists methods

# Add an item in list
marks.append(0)
print(marks)

# Remove last element from list
marks.pop()
print(marks)


# To remove element from position give index at pop(index)


# To append a list at the end of another list use extend
extra_marks = [2, 1, 1]
marks.extend(extra_marks)
print(marks)
# https://www.w3schools.com/python/python_ref_list.asp
