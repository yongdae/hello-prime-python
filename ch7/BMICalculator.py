# 사용자 몸무게 입력
weight = eval(input("몸무게를 입력하세요.(예, 75.4): "))

# 사용자 키 입력
height = eval(input("키를 입력하세요.(예, 180): "))

# BMI 계산
heightMeter = height / 100

bmi = weight / (heightMeter * heightMeter)

# 결과 출력

message = "당신은 "

if bmi < 18.5:
    message += "저체중"
elif bmi < 25:
    message += "정상"
elif bmi < 30:
    message += "과체중"
else:
    message += "비만"

print(message + "입니다.")