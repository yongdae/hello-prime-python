from CircleFromGeometricObject import Circle
from RectangleFromGeometricObject import Rectangle


def displayObject(g):
    print(g.__str__())

def isSameArea(one, two):
    return one.getArea() == two.getArea()

class main():
    circle = Circle(4)
    rectangle = Rectangle(1, 3)
    displayObject(circle)
    displayObject(rectangle)

    print("원과 사각형의 크기가 같습니까?", isSameArea(circle, rectangle))

main()