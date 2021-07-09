class Tomato:
    states = ['Pod', 'Green', 'Yellow', 'Ripe']

    def __init__(self, index, state=states[0]):
        self._index = index
        self._state = state

    def get_state(self):
        return self._state

    def grow(self):
        index = Tomato.states.index(self._state)
        if index < (len(Tomato.states)-1):
            self._state = Tomato.states[index + 1]
        else:
            return 'Томат уже созрел'
        return self._state

    def is_ripe(self):
        if self._state == 'Ripe':
            return True
        else:
            return False

    def __str__(self):
        return f'Томат на стадии: {self._state}'


class TomatoBush:
    def __init__(self, amount):
        self._tomatoes = []
        for i in range(amount):
            self._tomatoes.append(Tomato(input('Vvedite index: ')))

    def all_grow(self):
        for i in self._tomatoes:
            i.grow()

    def all_ripe(self):
        for i in self._tomatoes:
            if not i.is_ripe():
                return False
        return True

    def give_away_all(self):
        self._tomatoes = []

    def __str__(self):
        for i in self._tomatoes:
            print(i)
        return ''


class Gardener:
    def __init__(self, name, tomato):
        self._name = name
        self._plant = tomato

    def work(self):
        print(f'Садовник работает, томат вырастает из {self._plant.state} в {self._plant.grow()}.')

    def harvest(self):
        if self._plant.is_ripe():
            print('Пора собирать урожай.')
        else:
            print('Томат еще не вырос.')


tomato1 = Tomato('1')
print(tomato1.state)
gardener1 = Gardener('John', tomato1)
gardener1.work()
gardener1.work()
gardener1.work()
gardener1.work()