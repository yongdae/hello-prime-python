# 서식화
print("서식화")
print(format(57.467657, "2.2f"))
print(format(57.467657, "10.2f"))
print(format(12345678.923, "10.2f"))
print(format(57.4, "10.2f"))
print(format(57, "10.2f"))
print()

# 백분율
print("백분율")
print(format(0.53457, "10.2%"))
print(format(0.0033923, "10.2%"))
print()

# 서식정렬
print("서식 정렬")
print(format(57.467657, "10.2f"))
print(format(57.467657, "<10.2f"))
print(format(57.467657, ">10.2f"))
print()

# 정수 서식화
print("정수 서식화")
print(format(59832, "10d"))
print(format(59832, "<10d"))