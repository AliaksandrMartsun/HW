number = ""
while not number.isdigit():
    number = input()
sum = 0
mult = 1

for i in number:
    sum += int(i)
    mult *= int(i)
print(sum)
print(mult)