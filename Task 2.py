class Car:

    def __init__(self, mark, model, release_year):
       self.mark = mark
       self.model = model
       self.release_year = release_year

    __speed = 0

    def acceleration(self):
        self.__speed += 20
        print(self.__speed)

    def brake(self):
        self.__speed = 0
        print(self.__speed)


new_car = Car('Mercedes-Benz', 'E-class', '2020')
new_car.acceleration()
new_car.acceleration()
new_car.brake()
