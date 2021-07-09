with open('text_1.txt', 'w') as f:
    n = int(input("n = "))
    for i in range(n):
        f.writelines(input("Enter string: ") + '\n')
