from tkinter import *


class WidgetsDemo:
    def __init__(self):
        window = Tk()
        window.title("위젯 데모")

        frame1 = Frame(window)
        frame1.pack()

        self.v1 = IntVar()
        cbtBold = Checkbutton(
            frame1, text="굵게", variable=self.v1, command=self.processCheckButton)

        self.v2 = IntVar()
        rbRed = Checkbutton(frame1, text="빨간색", bg="red",
                            variable=self.v2, onvalue=1, command=self.processRadioButton)
        rbYellow = Checkbutton(frame1, text="노랑색", bg="yellow",
                               variable=self.v2, onvalue=2, command=self.processRadioButton)

        cbtBold.grid(row=1, column=1)
        rbRed.grid(row=1, column=2)
        rbYellow.grid(row=1, column=3)

        frame2 = Frame(window)
        frame2.pack()

        label = Label(frame2, text="이름을 입력하세요:")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable=self.name)
        btGetName = Button(frame2, text="이름 가져오기",
                           command=self.processButton)
        message = Message(frame2, text="위젯 데모입니다.")

        label.grid(row=1, column=1)
        entryName.grid(row=1, column=2)
        btGetName.grid(row=1, column=3)
        message.grid(row=1, column=4)

        text = Text(window)
        text.pack()

        text.insert(END, "팁\nTkinter를 학습하는 최고의 방법은 잘 짜여진 ")
        text.insert(END, "예제를 세세히 읽고 애플리케이션을 생성하는데 ")
        text.insert(END, "직접 사용해 보는 것이다. ")

        window.mainloop()

    def processCheckButton(self):
        print("체크 버튼이" + ("선택되었습니다." if self.v1.get() == 1 else "해제되었습니다."))

    def processRadioButton(self):
        print(("빨간색" if self.v2.get() == 1 else "노란색"), " 이 선택되었습니다.")

    def processButton(self):
        print("당신의 이름은", self.name.get() + "입니다.")


WidgetsDemo()
