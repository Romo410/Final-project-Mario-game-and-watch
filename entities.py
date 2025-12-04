class Package:
    def __init__(self, x, y):
        self.__x = 0
        self.__y = 0
        self.aux_pkg = 0
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be non-negative")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be non-negative")
        self.__y = value


    def pkg_move(self):
        self.aux_pkg += 1 
        if self.aux_pkg%7==0:
            if self.y == 160 or self.y == 160-32 or self.y == 160-32*2 or self.y == 160-32*3 or self.y ==160-32*4:
                self.x -= 10
            else:
                self.x += 10 
        
class Conveyor:
    def __init__(self, x, y, length, direction):
        self.__x = 0
        self.__y = 0
        self.x = x
        self.y = y
        self.length = length
        self.direction = direction 
        self.packages = []

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be non-negative")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be non-negative")
        self.__y = value

class Truck:
    def __init__(self, x, y):
        self.__x = 0
        self.__y = 0
        self.x = x
        self.y = y
        self.capacity = 8
        self.load = 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be non-negative")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be non-negative")
        self.__y = value
