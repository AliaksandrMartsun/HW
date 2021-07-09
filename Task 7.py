a = [1, 2, 3, 4, 5, 6, 7]
print(a)
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(a)
