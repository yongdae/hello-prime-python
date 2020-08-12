# 세 수를 입력 받는다.

number1, number2, number3 = eval(input("세 수를 입력해주세요: "))

if number1 > number2:
    if number1 > number3:
        print("가장 큰 수는", str(number1) + "입니다.")
    else:
        print("가장 큰 수는", str(number3) + "입니다.")
else:
    if number2 > number3:
        print("가장 큰 수는", str(number2) + "입니다.")
    else:
        print("가장 큰 수는", str(number3) + "입니다.")
