while True:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    sing = input("Enter sing: ")
    if sing == "+":
        print("Z = ", x + y)
    elif sing == "-":
        print("Z = ", x - y)
    elif sing == "*":
        print("Z = ", x * y)
    elif sing == "/":
        if y != 0:
            print("Z = ", x / y)
        else:
            print("Division by 0 is not allowed")
    elif sing == "0":
        print()
        break
    else:
        print("You entered nothing")
