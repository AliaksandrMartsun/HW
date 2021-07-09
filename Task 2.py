from datetime import datetime
from datetime import timedelta
import json

with open('dz.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    today = datetime.strptime("01/05/2021", "%d/%m/%Y")
    age_ = timedelta(days=7665)
    data_birth = datetime.strptime("01/06/2001", "%d/%m/%Y")
    all_height = 0
    personal_21 = 0
    for i in data:
        if today - datetime.strptime(i["birthday"], "%d/%m/%Y") >= timedelta(days=7665):
            all_height += i['height']
            personal_21 += 1
print(all_height / personal_21)
