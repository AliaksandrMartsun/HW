a = {"test": "test_value", "europe": "eur", "dollar": "usd", "ruble": "rub", "c": "b"}
print(a)
for i in list(a):
    a1 = f'{i}{len(i)}'
    a[a1] = a.pop(i)
print(a)