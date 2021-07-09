class Gun:

    def __init__(self, name, range, cartridges, bullets):
        self.__name = name
        self.__range = range
        self.__cartridges = cartridges
        self.__full_bullets = bullets
        self.__bullet = bullets

    def shoot(self):
        self.__full_bullets -= 1
        print("In the clip", self.__full_bullets, "bullets")
        if self.__full_bullets == 0:
            print("Change the clip")

    def cooldown(self):
        return print(self.__bullet)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, new_range):
        self.__range = new_range

    @property
    def cartridges(self):
        return self.__cartridges

    @cartridges.setter
    def cartridges(self, new_cartridges):
        self.__cartridges = new_cartridges

    @property
    def full_bullets(self):
        return self.__full_bullets

    @full_bullets.setter
    def full_bullets(self, new_full_bullets):
        self.__full_bullets = new_full_bullets

    @property
    def bullet(self):
        return self.__bullet

    @bullet.setter
    def bullet(self, new_bullet):
        self.__bullet = new_bullet


p_m = Gun('Пистолет Макарова', 350, 8, 3)
print(p_m.name)
print(p_m.range)
print(p_m.cartridges)
print(p_m.full_bullets)
p_m.shoot()
p_m.shoot()
p_m.shoot()
p_m.cooldown()
