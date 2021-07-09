def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(4))
