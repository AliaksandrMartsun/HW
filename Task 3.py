

def my_decor(func):
    def wrapper(arg):
        arg = [i for i in arg if i % 2 != 0 or i == 0]
        return func(arg)
    return wrapper

@my_decor
def my_list(any_list):
    for i in any_list:
        print(i)


lst = [2, 7, 9, 10, 45, 12, -12, 13, 0]
my_list(lst)
