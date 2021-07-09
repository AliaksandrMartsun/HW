import json
with open('dz.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    height = 0
    k = 0
    for i in data:
        if int(i['birthday'][-4:]) < 2000:
            height += i['height']
            k += 1
    print(height / k)
