from Circle import Circle


def main():
    circle1 = Circle()  # 반지름 1인 원을 생성한다.
    print("반지름이", circle1.radius, "인 원의 넓이는 ", circle1.getArea(), "입니다.")

    circle2 = Circle(25)  # 반지름 25인 원을 생성한다.
    print("반지름이", circle2.radius, "인 원의 넓이는 ", circle2.getArea(), "입니다.")

    circle3 = Circle(125)  # 반지름 125인 원을 생성한다.
    print("반지름이", circle3.radius, "인 원의 넓이는 ", circle3.getArea(), "입니다.")

    circle2.radius = 100  # 반지름을 100으로 다시 설정
    print("반지름이", circle2.radius, "인 원의 넓이는 ", circle2.getArea(), "입니다.")


main()
