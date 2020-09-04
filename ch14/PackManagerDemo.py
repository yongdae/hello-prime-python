from tkinter import *


class PackManagerDemo:
    def __init__(self):
        window = Tk()
        window.title("팩 관리자 데모")

        Label(window, text="파랑", bg="blue").pack()
        Label(window, text="빨강", bg="red").pack(fill=BOTH, expand=1)
        Label(window, text="초록", bg="green").pack(fill=BOTH)

        window.mainloop()

PackManagerDemo()
