# 사용자 입력
level = eval(input("몇단을 출력까요?"))

# 결과값 출력
for i in range(1, 10):
    print(i * level, end=' ')
