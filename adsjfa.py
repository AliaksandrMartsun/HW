class Student:
    estimations = {'math': [], 'physics': [], 'biology': []}

    def __init__(self, name, lastname, group):
        self._name = name
        self._lastname = lastname
        self._group = group
        self._estimations = {'math': [], 'physics': [], 'biology': []}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, new_lastname):
        self._lastname = new_lastname

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, new_group):
        self._group = new_group

    def add_estimation(self, subject, estimation):
        print(self._estimations)
        if subject == 'math':
            self._estimations[subject].append(estimation)
            print(self._estimations)
        elif subject == 'physics':
            self._estimations[subject].append(estimation)
            print(self._estimations)
        else:
            self._estimations[subject].append(estimation)
            print(self._estimations)


Slava1 = Student('Ivan', 'Ivanov', 5)
Alina1 = Student('Alina', 'Martsun', 4)
Sasha1 = Student('Sasha', 'Martsun', 3)
Max1 = Student('Max', 'sladjfk', 4)

students = [Slava1, Alina1, Sasha1, Max1]

import json

with open('students.json', 'w') as f:
    lst = []
    for i in students:
        tmp_dict = {}
        tmp_dict['Name'] = i.name
        tmp_dict['Lastname'] = i.lastname
        tmp_dict['Group'] = i.group
        lst.append(tmp_dict)
    json.dump(lst, f, ensure_ascii=False, indent=4)

