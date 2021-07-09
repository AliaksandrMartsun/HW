

def my_class(a, b, c):
        class_1 = a / 2
        if class_1 % 2 == 0:
            class_1 += 0.5
        class_2 = b / 2
        if class_2 % 2 == 0:
            class_2 += 0.5
        class_3 = c / 2
        if class_3 % 2 == 0:
            class_3 += 0.5
        sum = class_1 + class_2 + class_3
        return sum


print(my_class(30, 20, 23))
