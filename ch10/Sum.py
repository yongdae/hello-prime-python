def sum(start, end):
    result = 0

    for number in range(start, end + 1):
        result += number

    return result


result = sum(1, 10)
print("1부터 10까지의 합은", result, "입니다.")


result = sum(20, 38)
print("20부터 38까지의 합은", result, "입니다.")


result = sum(35, 50)
print("35부터 50까지의 합은", result, "입니다.")
