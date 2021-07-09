

def my_func(*args):
    summ = 0
    for i, elem in enumerate(args):
        summ += args[i] * i
    return summ


a = my_func(1, 2, 3, 4, 5)
print(a)
