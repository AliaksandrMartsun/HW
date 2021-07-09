

def power(a, n):
    result = a
    for i in range(n - 1):
        result *= a
    return result


print(power(2, 4))
