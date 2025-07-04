my_nums = [1, 2, 3, 4, 5]


def square(x):
    return x * x


square_nums = list(map(square, my_nums))
print(square_nums)
