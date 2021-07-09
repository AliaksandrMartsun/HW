from random import randint
a = []
for i in range(0, 10):
    a.append(randint(0, 1000))
print(a)

for i in a:
    max_a = a.index(max(a))
    min_a = a.index(min(a))
    a[min_a], a[max_a] = a[max_a], a[min_a]
print(a)
