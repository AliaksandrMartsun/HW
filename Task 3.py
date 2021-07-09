with open('text_1.txt', 'r') as f, open('text_2.txt', 'w') as f1, open('text_3.txt', 'w') as f2:
    f = f.readlines()
    result = list(f)[1::2]
    f1.writelines(result)
    result_2 = list(f)[0::2]
    f2.writelines(result_2)
