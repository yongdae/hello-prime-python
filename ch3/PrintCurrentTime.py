import time

currentTime = time.time()

totalSeconds = int(currentTime)

currentSeconds = totalSeconds % 60

totalMinutes = totalSeconds // 60

currentMinute = totalMinutes % 60

totalHours = totalMinutes // 60

currentHours = totalHours % 24

print("현재 시간은 ", currentHours, ":", currentMinute, ":", currentSeconds, " 입니다.")