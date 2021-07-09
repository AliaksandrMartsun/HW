func = lambda **kwargs: {key * 2: i for key, i in kwargs.items()}
a = func(qwe=5, qaz=9, qwert=3)
print(a)
