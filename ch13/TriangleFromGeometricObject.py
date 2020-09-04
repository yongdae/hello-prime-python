import math
from GeometricObject import GeometricObject


class Triangle(GeometricObject):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def setSide1(self, side1):
        self.__side1 = side1

    def getSide2(self):
        return self.__side2

    def setSide2(self, side2):
        self.__side2 = side2

    def getSide3(self):
        return self.__side3

    def setSide3(self, side3):
        self.__side3 = side3

    def getArea(self):
        sum = (self.__side1 + self.__side2 + self.__side3)
        return math.sqrt(sum * (sum - self.__side1) * (sum - self.__side2) * (sum - self.__side3))
    
    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return super().__str__() + " 변1:" + str(self.__side1) + " 변2:" + str(self.__side2) + " 변3:" + str(self.__side3)
