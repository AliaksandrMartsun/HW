from random import randint
n = 0
a = randint(0, 1000)
print("Guessed number - ", a)
while n < 5:
    n += 1
    number = int(input("Enter number: "))
    if number == a:
        print("You guessed the number ")
        break
    elif number > a:
        print("This number less ")
    elif number < a:
        print("This number more ")
    else:
        print("You didn't enter number ")
