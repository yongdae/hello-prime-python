# 사용자 입력
number = eval(input("정수를 입력하세요: "))

sum = 0

for i in range(1, number + 1):
    if i % 4 == 0:
        continue
    sum += i

print("4의 배수를 제외한", number, "까지의 합은", sum, " 입니다.")
