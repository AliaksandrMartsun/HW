a = str(input("Enter number: "))
summ = 0
mult = 1
for i in a:
    summ += int(i)
    mult *= int(i)
print(summ)
print(mult)
