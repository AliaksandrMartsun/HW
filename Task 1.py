

def string(c):
    a = ''
    for i in c:
        if i == i.lower():
            a += i
    return a


print(string("Привет, как Дела. Что будешь делать?"))
