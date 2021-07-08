a = [1, 2, 3, 4, 5]
steps = int(input())
b = []
for i in range(steps, len(a)):
    b.append(a[i])
for i in range(0, steps):
    b.append(a[i])
print(b)