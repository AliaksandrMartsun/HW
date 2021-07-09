import json

with open('stud.json') as f1, open('rooms1.json') as f2, open('result.json', 'w') as result:
    students = json.load(f1)
    rooms = json.load(f2)
    for room in rooms:
        room['students'] = []
    # for room in rooms:
    #     for student in students:
    #         if room['id'] == student['room']:
    #             room['students'].append({'id': student['id'], 'name': student['name']})
    for student in students:
        rooms[student['room']]['students'].append({'id': student['id'], 'name': student['name']})
    json.dump(rooms, result, indent=4)
