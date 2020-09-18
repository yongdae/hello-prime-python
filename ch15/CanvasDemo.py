from tkinter import *


class CanvasDemo:
    def __init__(self):
        window = Tk()  # 창을 생성한다.
        window.title("캔버스 데모")  # 제목을 설정한다.

        # 창에 갠버스를 배친한다.
        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        # 프레임에 버튼을 배치한다.
        frame = Frame(window)
        frame.pack()

        btRectangle = Button(frame, text="직사각형", command=self.displayRect)
        btOval = Button(frame, text="타원", command=self.displayOval)
        btArc = Button(frame, text="호", command=self.displayArc)
        btPolygon = Button(frame, text="다각형", command=self.displayPolygon)
        btLine = Button(frame, text="선분", command=self.displayLine)
        btString = Button(frame, text="문자열", command=self.displayString)
        btClear = Button(frame, text="삭제하기", command=self.clearCanvas)

        btRectangle.grid(row=1, column=1)
        btOval.grid(row=1, column=2)
        btArc.grid(row=1, column=3)
        btPolygon.grid(row=1, column=4)
        btLine.grid(row=1, column=5)
        btString.grid(row=1, column=6)
        btClear.grid(row=1, column=7)

        window.mainloop()  # 이벤트 루프를 생성한다.

    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")

    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill="red", tags="oval")

    def displayArc(self):
        self.canvas.create_arc(10, 10, 190, 90, start=0,
                               extent=90, width=8, fill="red", tags="arc")

    def displayPolygon(self):
        self.canvas.create_polygon(10, 10, 190, 90, 30, 50, tags="polygon")

    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, fill="red", tags="line")
        self.canvas.create_line(10, 90, 190, 10, width=9,
                                arrow="last", activefill="blue", tags="line")

    def displayString(self):
        self.canvas.create_text(
            85, 40, text="안녕, 나는 문자열이야", font="rnfflacp 10 bold underline", tags="string")

    def clearCanvas(self):
        self.canvas.delete("rect", "oval", "arc", "polygon", "line", "string")


CanvasDemo()
