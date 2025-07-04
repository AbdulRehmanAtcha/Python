from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# Internal working of reduce in this case
# [3,3,4,5,6]
# [6,4,5,6]
# [10,5,6]
# [15,6]
# [21]

a = reduce(lambda x, y: x + y, numbers)
print(a)
