class Car:
    def __init__(self, mark, model, year, speed=0):
        self.__mark = mark
        self.__model = model
        self.__year = year
        self.__speed = speed
        self.__engine = False

    def turn_engine(self):
        self.__engine = True

    def up_speed(self):
        if self.__engine:
            self.__speed += 10
        else:
            print("Turn on engine")

    def down_speed(self):
        if self.__engine:
            if self.__speed >= 10:
                self.__speed -= 10
            else:
                self.__speed = 0
        else:
            print("Turn on engine")

    def get_speed(self):
        return f'{self.__speed} km/h, {self.get_step()} step'

    def get_step(self):
        if self.__speed == 0:
            return 'N'
        elif self.__speed <= 15:
            return '1'
        elif self.__speed <= 30:
            return '2'
        elif self.__speed <= 45:
            return '3'
        elif self.__speed <= 60:
            return '4'
        elif self.__speed <= 75:
            return '5'
        else:
            return '6'


car_1 = Car('Mercedes-Benz', 'E-class', '2020')
car_1.turn_engine()
car_1.up_speed()
car_1.down_speed()
print(car_1.get_step())
print(car_1.get_speed())
