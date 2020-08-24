number = eval(input("정수를 입력하세요: "))

isPrime = True

for i in range(1, number):
    if number % i == 0:
        isPrime = False
        break

if isPrime:
    print(number, "은 소수입니다.")
else:
    print(number, "은 소수가 아닙니다.")
