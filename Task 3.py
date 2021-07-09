class Student:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.marks = []
        self.info = []

    def append_mark(self, mark):
        self.marks.append(mark)

    def append_info(self, info):
        self.info.append(info)

    def __str__(self):
        return f'Name: {self.name} {self.last_name}, marks: {self.marks}, ' \
               f'info: {self.info}'


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def del_student(self):
        for i, elem in enumerate(self.students):
            print(f'{i}. {elem}')
        index = int(input('Укажите номер студента, которого хотите удалить:'))
        del self.students[index]


class Teacher:
    def __init__(self, name, last_name, group):
        self.name = name
        self.last_name = last_name
        self.group = group

    def teach(self, info):
        for student in self.group.students:
            student.append_info(info)

    def rate_student(self):
        for i, elem in enumerate(self.group.students):
            print(f'{i}. {elem}')
        mark = int(input('Введите оценку: '))
        index = int(input('Введите номер студента: '))
        self.group.students[index].append_mark(mark)


st1 = Student('John', 'Doe')
st2 = Student('Alex', 'Doe')
st3 = Student('Frank', 'Doe')
group1 = Group('overone')
group1.add_student(st1)
group1.add_student(st2)
group1.add_student(st3)
teacher1 = Teacher('Teacher','Teacher', group1)
teacher1.teach('some info')
teacher1.teach('some info 2')
teacher1.rate_student()
teacher1.rate_student()
group1.del_student()
print(st1)
print(st3)