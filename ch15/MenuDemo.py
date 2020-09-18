from tkinter import *


class MenuDemo:
    def __init__(self):
        window = Tk()
        window.title("팝업 메뉴 데모")

        menubar = Menu(window)
        window.config(menu=menubar)

        openMenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="선택", menu=openMenu)

        openMenu.add_command(label="선 그리기", command=self.displayLine)
        openMenu.add_command(label="타원 그리기", command=self.displayOval)
        openMenu.add_command(label="사격형 그리기", command=self.displayRect)
        openMenu.add_command(label="지우기", command=self.clearCanvas)

        # 창에 갠버스를 배친한다.
        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        window.mainloop()

    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")

    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 90, fill="red", tags="oval")

    def displayLine(self):
        self.canvas.create_line(10, 10, 190, 90, fill="red", tags="line")
        self.canvas.create_line(10, 90, 190, 10, width=9,
                                arrow="last", activefill="blue", tags="line")

    def clearCanvas(self):
        self.canvas.delete("rect", "oval", "line")


MenuDemo()
