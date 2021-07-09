a = list(input())
n = 3
for i in range(n):
    a.append(input())


def my_func(name):
    print(f"Hello, {name}")


for i in a:
    my_func(i)
