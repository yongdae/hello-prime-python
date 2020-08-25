from TV import TV


def main():
    tv1 = TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolumeLevel(3)

    tv2 = TV()
    tv2.turnOn()
    tv2.channelUp()
    tv2.channelUp()
    tv2.volumeUp()

    print("tv1의 채널은", tv1.getChannel(),
          "이고 음량 크기는", tv1.getVolumeLevel(), "입니다.")

    print("tv2의 채널은", tv2.getChannel(),
          "이고 음량 크기는", tv2.getVolumeLevel(), "입니다.")

main()