import json
with open('stud.json', 'r') as f, open('rooms1.json', 'r') as f1, open('Students.json', 'w') as f2:
    data_1 = json.load(f)
    data_2 = json.load(f1)
    for i in data_1:
        for j in data_2:
            if i['room'] == j['id']:
                j['students'] = []
                j['students'] += [i]
    for i in data_1:
        for j in data_2:
            if i['room'] == j['id']:
                if i not in j['students']:
                    j['students'] += [i]

    json.dump(data_2, f2, ensure_ascii=False, indent=4)
