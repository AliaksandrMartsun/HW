import math
fact = math.factorial


def fact(n):
    if n % 2 == 0:
        for i in range(2, n + 1, 2):

        return fact(2*k) / (2**k * fact(k))
    else:
        return 2**k * fact(k)


a = int(input("Enter number: "))
print(fact(a))
