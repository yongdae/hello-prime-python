year = eval(input("출생년도를 입력하세요: "))

zodiactYear = year % 12

if(zodiactYear) == 0:
    print("원숭이")
elif(zodiactYear) == 1:
    print("닭")
elif(zodiactYear) == 2:
    print("개")
elif(zodiactYear) == 3:
    print("돼지")
elif(zodiactYear) == 4:
    print("쥐")
elif(zodiactYear) == 5:
    print("소")
elif(zodiactYear) == 6:
    print("범")
elif(zodiactYear) == 7:
    print("토끼")
elif(zodiactYear) == 8:
    print("용")
elif(zodiactYear) == 9:
    print("뱀")
elif(zodiactYear) == 10:
    print("말")
else:
    print("양")
