

def my_decor(func):
    def wrapper(*args):
        return func(*args[::-1])
    return wrapper


@my_decor
def my_list(*args):
    for i in args:
        print(i)


my_list(1, 5, 7)
