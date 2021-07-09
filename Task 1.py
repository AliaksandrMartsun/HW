class House:

    def __init__(self, room, floors, square):
        self.__room = room
        self.__floors = floors
        self.__square = square

    def rooms(self, room):
        if self.__room:
            print(self.__room, "rooms")
        else:
            print("You didn't enter the number of rooms")

    def floor(self, floors):
        if self.__floors:
            print(self.__floors, "floors")
        else:
            print("you didn't enter the number of floors")

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, new_room):
        self.__room = new_room

    @property
    def floors(self):
        return self.__floors

    @floors.setter
    def floors(self, new_floors):
        self.__floors = new_floors

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, new_square):
        self.__square = new_square


my_house = House(5, 2, 110)
print(my_house.floors)
print(my_house.room)
print(my_house.square)
my_house.rooms(5)
my_house.floor(2)



