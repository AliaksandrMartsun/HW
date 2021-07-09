

def my_str(b):
    new_str = ''
    for elem in b:
        if elem.isalpha() or elem == ' ':
            new_str += elem
    return new_str.split()


str = 'Hello1, how are you.'
print(my_str(str))
