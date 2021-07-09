

def bank(a, years):
    for i in range(years):
        a += a * 0.1
        print(a)
    return a


res = bank(1000, 2)
print(res)
