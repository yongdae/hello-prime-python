import math


class CirclePrivate:

    # circle 객체를 생선한다.
    def __init__(self, radius=1):
        self.__radius = radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius * math.pi

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius
