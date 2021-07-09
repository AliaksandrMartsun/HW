from random import randint
a = []
n = int(input("Enter number: "))
for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(randint(1, 100))
for i in a:
    print(i)
for i in range(n):
    max_n = a[i][0]
    temp_j = 0
    for j in range(n):
        if max_n < a[i][j]:
            max_n = a[i][j]
            temp_j = j
    a[i][i], a[i][temp_j] = a[i][temp_j], a[i][i]
print(a)
