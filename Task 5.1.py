from random import randint
myList = []
my_result = list()
a = 0
while a < 19:
    myList.append(randint(1, 100))
    a += 1
print(myList)
print(max(myList))
for number in myList:
    if number % 2 == 0:
        my_result.append(max(myList))
    else:
        my_result.append(number)

print(my_result)
