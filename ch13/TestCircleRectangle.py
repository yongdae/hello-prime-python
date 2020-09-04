from CircleFromGeometricObject import Circle
from RectangleFromGeometricObject import Rectangle


class main():
    circle = Circle(1.5)
    print("원", circle)
    print("넓이는", circle.getArea(), "입니다")
    print("지름은", circle.getPerimeter(), "입니다")

    rectangle = Rectangle(2, 4)
    print("\n사각형", rectangle)
    print("넓이는", rectangle.getArea(), "입니다")
    print("둘레는", rectangle.getPerimeter(), "입니다")

main()