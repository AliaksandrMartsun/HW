with open('text_1.txt', 'r') as f:
    f = f.readlines()
    for string in f:
        counter = 0
        for i in string:
            if i.isalpha():
                counter += 1
        print(f'{string}, {counter} букв {len(string.split(" "))} слов')
