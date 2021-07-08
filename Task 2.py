a = int(input("input first value:"))
b = int(input("input second value:"))
c = int(input("input third value:"))
if a > b and a > c:
    print("Bigger number: ", a)
elif b > a and b > c:
    print("Bigger number: ", b)
else:
    print("Bigger number: ", c)