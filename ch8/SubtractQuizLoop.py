import random

number1 = random.randint(0, 9)  # 0 ~ 9 랜덤 숫자를 생성한다.
number2 = random.randint(0, 9)  # 0 ~ 9 랜덤 숫자를 생성한다.

if (number1 < number2):
    number1, number2 = number2, number1

# 사용자로부터 답을 입력받는다.
answer = eval(input(str(number1) + " - " + str(number2) + " 은/는 얼마입니까? :"))

while number1 - number2 != answer:
    answer = eval(input(str(number1) + " - " + str(number2) + " 은/는 얼마입니까? :"))

print("정답입니다.")
