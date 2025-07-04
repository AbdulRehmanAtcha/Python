# def is_even(x):
#     if x % 2 == 0:
#         return True
#     return False


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# new_nums = list(filter(is_even, nums))
# print(new_nums)


# OR
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_nums = list(filter(lambda x: x % 2 != 0, nums))
print(new_nums)
