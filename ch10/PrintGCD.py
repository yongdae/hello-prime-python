# 두 정수를 입력 받는다.
n1, n2 = eval(input("두 정수를 입력하세요: "))
gcd = 1
k = 2

while k <= n1 and k < n2:
    if n1 % k == 0 and n2 % k == 0:
        gcd = k # gcd를 갱신한다.
    k += 1

print(n1, "와/과", n2, "의 GCD는", gcd, "입니다.")