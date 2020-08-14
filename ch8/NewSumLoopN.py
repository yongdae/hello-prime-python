# 사용자 입력
number = eval(input("정수를 입력하세요 (0을 입력하면 종료): "))

sum = 0

while number != 0:
    sum = sum + number
    number = eval(input("정수를 입력하세요 (0을 입력하면 종료): "))

print("합계는 = ", sum, " 입니다.")
