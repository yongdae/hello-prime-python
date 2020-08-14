import random

number = random.randint(0, 100)

print("0 과 100 사이 미지의 숫자를 맞혀보세요.")

guess = eval(input("얼마일까요?: "))

while number != guess:

    if guess > number:
        print("입력한 값이 큽니다.")
    elif guess < number:
        print("입력한 값이 작습니다.")

    guess = eval(input("얼마일까요?: "))

print("정답을 맞추셨습니다. 미지의 숫자는 =", number, " 입니다.")
