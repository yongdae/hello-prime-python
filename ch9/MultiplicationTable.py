print(format("구구단표", ">20s"))

print("  |", end="")  # 숫자 표머리를 출력한다.
for j in range(1, 10):
    print("  ", j, end="")
print()
print("------------------------------------------")

for i in range(1, 10):  # 구구단 표를 출력한다.
    print(i, "|", end="")
    for j in range(1, 10):
        # 곱셈 결과를 출력하고 정렬한다.
        print(format(i * j, '4d'), end="")
    print()  # 새로운 행에서 시작한다.
