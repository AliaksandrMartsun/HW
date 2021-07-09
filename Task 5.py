from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    limit = sqrt(n)
    a = 2
    while a <= limit:
        if n % a == 0:
            return False
        a += 1
    return True


for i in range(10):
    num = int(input())
    print(is_prime(num))
