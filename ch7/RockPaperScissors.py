import random

# 컴퓨터 가위, 바위, 보 생성
computer = random.randint(0, 2)

# 사용자 가위, 바위, 보 입력
user = eval(input("가위(0), 바위(1), 보(2) 를 입력하세요: "))

# 평가하기
if computer == 0:
    if user == 0:
        print("컴퓨터는 가위, 당신도 가위 비겼습니다.")
    elif user == 1:
        print("컴퓨터는 가위, 당신은 바위 이겼습니다.")
    else:
        print("컴퓨터는 가위, 당신은 보 졌습니다.")
elif computer == 1:
    if user == 0:
        print("컴퓨터는 바위, 당신도 가위 졌습니다.")
    elif user == 1:
        print("컴퓨터는 바위, 당신은 바위 비겼습니다.")
    else:
        print("컴퓨터는 바위, 당신은 보 이겼습니다.")
elif computer == 2:
    if user == 0:
        print("컴퓨터는 보, 당신도 가위 이겼습니다.")
    elif user == 1:
        print("컴퓨터는 보, 당신은 바위 졌습니다.")
    else:
        print("컴퓨터는 보, 당신은 보 비겼습니다.")