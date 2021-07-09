from random import randint
N = 19
myList = []
my_result = list()
for i in range(N):
    myList.append(int(randint(1, 100)))
print(myList)
print(max(myList))

for i in myList:
    if i % 2 == 0:
        my_result.append(max(myList))
    else:
        my_result.append(i)
print(my_result)
