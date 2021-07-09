

def bank(a, years):
    money = a * 1.1 ** (years)
    return money


res = bank(1000, 1)
print(res)