from tkinter import *


class GridManagerDemo:
    def __init__(self):
        window = Tk()
        window.title("그리드 관리자 데모")

        message = Message(window, text="이 메시지 위젯은 3개의 행과 2개의 열을 차지한다.")
        message.grid(row=1, column=1, rowspan=3, columnspan=2)

        Label(window, text="이름:").grid(row=1, column=3)
        Entry(window).grid(row=1, column=4, padx=5, pady=5)

        Label(window, text="성:").grid(row=2, column=3)
        Entry(window).grid(row=2, column=4)

        Button(window, text="이름 가져오기").grid(
            row=3, padx=5, pady=5, column=4, sticky=E)

        window.mainloop()


GridManagerDemo()
