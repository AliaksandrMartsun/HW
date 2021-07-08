import math

a = float(input("input first value leg: "))
b = float(input("input second value leg: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
d = (a * b) / 2
print("Hypotenuse: ", c)
print("The area of the right triangle: ", d)