#code
class Shoe():
    def __init__(self, t, c="undefined"):
        self.__type = t
        self.__color = c

    def get_type(self):
        print(self.__type)

    def get_color(self):
        print(self.__color)

    def set_color(self, c):
        self.__color = c
        print(f'The color of the {self.__type.lower()} is {c.lower()}.')
\
class Oxford(Shoe):
    def __init__(self):
        super().__init__("Oxfords")

class Sneaker(Shoe):
    def __init__(self):
        super().__init__("Sneakers")

o = Oxford()
s = Sneaker()

o.get_type()
s.get_type()


o.set_color("Black")
s.set_color("Brown")