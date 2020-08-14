# 사용자 입력
number = eval(input("정수를 입력하세요: "))

sum = 0
count = 1

while count <= number:
    sum = sum + count
    count += 1

print(number, "까지의 합은", sum, "입니다.")
