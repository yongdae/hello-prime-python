from tkinter import *


class NewMenuDemo:
    def __init__(self):
        window = Tk()
        window.title("메뉴 데모")

        menubar = Menu(window)
        window.config(menu=menubar)

        openMenu = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="연산", menu=openMenu)

        openMenu.add_command(label="더하기", command=self.add)
        openMenu.add_command(label="빼기", command=self.subtract)
        openMenu.add_command(label="곱하기", command=self.multiply)
        openMenu.add_command(label="나누기", command=self.divide)

        # 창에 갠버스를 배친한다.
        self.canvas = Canvas(window, width=200, height=100, bg="white")
        self.canvas.pack()

        exitmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="나가기", menu=exitmenu)
        openMenu.add_command(label="더하기", command=window.quit)

        plusImage = PhotoImage(file="image/plus.gif")
        minusImage = PhotoImage(file="image/minus.gif")
        timesImage = PhotoImage(file="image/times.gif")
        divideImage = PhotoImage(file="image/divide.gif")

        frame = Frame(window)
        frame.pack()

        Checkbutton(frame, image=koImage).pack(side=LEFT)
        Checkbutton(frame, image=ukImage).pack(side=LEFT)
        Radiobutton(frame, image=crossImage).pack(side=LEFT)
        Radiobutton(frame, image=circleImage).pack(side=LEFT)

        window.mainloop()

    def add(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags="rect")

    def subtract(self):
        self.canvas.create_oval(10, 10, 190, 90, fill="red", tags="oval")

    def multiply(self):
        self.canvas.create_line(10, 10, 190, 90, fill="red", tags="line")
        self.canvas.create_line(10, 90, 190, 10, width=9,
                                arrow="last", activefill="blue", tags="line")

    def divide(self):
        self.canvas.delete("rect", "oval", "line")


NewMenuDemo()
