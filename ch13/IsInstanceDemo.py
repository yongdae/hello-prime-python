from CircleFromGeometricObject import Circle
from RectangleFromGeometricObject import Rectangle
from TriangleFromGeometricObject import Triangle

def displayObject(g):
    print(g.__str__())
    print("넓이는", g.getArea(), "입니다.")
    print("둘레는", g.getPerimeter(), "입니다.")

    if isinstance(g, Circle):
        print("지름은", g.getDiameter(), "입니다.")
    elif isinstance(g, Rectangle):
        print("폭은", g.getWidth(), "입니다.")
        print("높이는", g.getHeight(), "입니다.")
    elif isinstance(g, Triangle):
        print("변 1은", g.getSide1(), "입니다.")
        print("변 2는", g.getSide2(), "입니다.")
        print("변 3은", g.getSide3(), "입니다.")


class main():
    circle = Circle(4)
    rectangle = Rectangle(1, 3)
    triangle = Triangle(4, 5, 8)

    print("원 ...")
    displayObject(circle)

    print("삼각형 ...")
    displayObject(triangle)

    print("사각형 ...")
    displayObject(rectangle)

main()