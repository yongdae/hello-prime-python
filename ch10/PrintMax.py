def max(num1, num2):  # 두 수 중 큰수를 반환한다.
    if num1 > num2:
        result = num1
    else:
        result = num2
    return result


def main():
    n1, n2 = eval(input("두 수를 입력하세요: "))
    n3 = max(n1, n2)  # max 함수를 호출한다.
    print(n1, "와/과", n2, "중에서 큰수는", n3, "입니다.")


main()  # main 함수 실행
