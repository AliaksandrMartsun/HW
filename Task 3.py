n = 9
a = []
for i in range(10):
    a.append([])
    for j in range(i):
        a[i].append(1 + j)

for i in a:
    print(i)
