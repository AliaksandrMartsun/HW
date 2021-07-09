import json
with open('dz.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
    a = 0
    tmp_i = 0
    for i, elem in enumerate(text):
        if a < len(elem['languages']):
            a = len(elem['languages'])
            tmp_i = i
    print(text[tmp_i])
