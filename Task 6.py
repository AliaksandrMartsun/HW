counter = 0
numb = list[0]
for i, number in enumerate(list):
    if numb < number:
        numb = number
    else:
        numb = number
        if numb > list[i + 1] and i + 1 < number:
            counter += 1
