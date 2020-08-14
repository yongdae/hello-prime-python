import random
import time

numberOfQuestion = eval(input("문제의 개수를 결정하세요: "))

count = 0
correctCount = 0

startTime = time.time()

while numberOfQuestion != count:
    count += 1

    number1 = random.randint(0, 15)  # 0 ~ 15 랜덤 숫자를 생성한다.
    number2 = random.randint(0, 15)  # 0 ~ 15 랜덤 숫자를 생성한다.

    if (number1 < number2):
        number1, number2 = number2, number1

    # 사용자로부터 답을 입력받는다.
    answer = eval(input(str(number1) + " - " + str(number2) + " 은/는 얼마입니까? :"))

    if number1 - number2 == answer:
        print("정답입니다.")
        correctCount += 1
    else:
        print("틀렸습니다.", "정답은 = ", number1 - number2, " 입니다.")

endTime = time.time()
testTime = int(endTime - startTime)

print("정답의 개수는 ", numberOfQuestion, " 개 중 ", correctCount, " 입니다.")
print("수행시간은 ", testTime, " 초 입니다.")
