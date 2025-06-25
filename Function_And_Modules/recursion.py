def Fib(n):
    if n == 0 or n == 1:
        return n
    return Fib(n - 2) + Fib(n - 1)


res1 = Fib(7)
print(res1)
