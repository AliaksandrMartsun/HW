a = float(input("input first value: "))
b = float(input("input second value: "))
c = input("")
d = None
if c == "+":
    d = a + b
    print(d)
elif c == "-":
    d = a - b
    print(d)
elif c == "*":
    d = a * b
    print(d)
elif c == "/":
    d = a / b
    print(d)
else:
    print("Nothing sign")
