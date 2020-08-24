def pringGrade(score):
    if score >= 90.0:
        print("A")
    elif score >= 80.0:
        print("B")
    elif score >= 70.0:
        print("C")
    elif score >= 60.0:
        print("D")
    else:
        print("F")


def main():
    score = eval(input("점수를 입력하세요: "))
    print("성적은", end="")
    pringGrade(score)
    print("입니다.")


main()  # main 함수 실행
