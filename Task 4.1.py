a = input("Enter string: ")
b = len(a) / 2
if len(a) % 2 == 0:
    print(a[int(b) - 1:int(b) + 1])
    if a[int(b) - 1:int(b) + 1] == a[0:1]:
        print(a[2:-1])
    else:
        print("The letters are different")
elif len(a) % 2 != 0:
    print(a[int(b)])
    if a[int(b)] == a[0]:
        print(a[1:-1])
    else:
        print("The letters are different")
else:
    print("You entered an empty string")
