class Alphabet:
    def __init__(self, lang, letters):
        self.__lang = lang
        self.__letters = letters

    def print(self):
        print(self.__letters)

    def letters_num(self):
        return len(self.__letters)


alphabet_rus = Alphabet('rus', ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
                                'р', 'c', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я'])

alphabet_rus.print()
print(alphabet_rus.letters_num())
