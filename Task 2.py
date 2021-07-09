with open('text_1.txt', 'a') as f:
    for i in range(3):
        f.writelines(input('Enter string: ') + '\n')
