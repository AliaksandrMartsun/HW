with open('dz-task5.txt', 'r', encoding='utf-8') as f:
    f = f.readlines()
    summ = 0
    for string in f:
        string = string.split(" ")
        summ += int(string[1])
    print(summ / len(f))
