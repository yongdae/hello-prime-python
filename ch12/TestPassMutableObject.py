from CircleWithPrivateRadius import CirclePrivate


def main():
    circle = CirclePrivate()  # 반지름 1인 원을 생성한다.

    n = 5
    printAreas(circle, n)


def printAreas(c, times):
    print("반지름 \t\t넓이")
    while times >= 1:
        print(c.getRadius(), "\t\t", c.getArea())
        c.setRadius(c.getRadius() + 1)
        times -= 1


main()
