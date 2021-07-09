

def factoliall(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)


b = int(input())
print(factoliall(b))
