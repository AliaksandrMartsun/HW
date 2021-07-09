import json
with open('dz-task5.txt', 'r', encoding='utf-8') as f, open('dz-task5.json', 'w', encoding='utf-8') as f1:
    f = f.readlines()
    lst = []
    for string in f:
        tmp_dict = {}
        string = string.split( )
        tmp_dict['name'] = string[0]
        tmp_dict['rate'] = int(string[1])
        lst.append(tmp_dict)
    json.dump(lst, f1, ensure_ascii=False, indent=4)
