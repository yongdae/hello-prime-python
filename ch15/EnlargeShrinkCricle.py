from tkinter import *


class EnlargeShrinkCricle:
    def __init__(self):
        self.radius = 50

        window = Tk()
        window.title("원 제어 데모")

        # 창에 갠버스를 배친한다.
        self.canvas = Canvas(window, width=200, height=200, bg="white")
        self.canvas.pack()

        self.canvas.create_oval(100 - self.radius, 100 - self.radius,
                                100 + self.radius, 100 + self.radius, tags="oval")

        self.canvas.bind("<Button-1>", self.increaseCircle)
        self.canvas.bind("<Button-2>", self.decreaseCircle)

        window.mainloop()

    def increaseCircle(self, event):
        self.canvas.delete("oval")

        if self.radius < 100:
            self.radius += 2

        self.canvas.create_oval(100 - self.radius, 100 - self.radius,
                                100 + self.radius, 100 + self.radius, tags="oval")

    def decreaseCircle(self, event):
        self.canvas.delete("oval")

        if self.radius > 2:
            self.radius -= 2

        self.canvas.create_oval(100 - self.radius, 100 - self.radius,
                                100 + self.radius, 100 + self.radius, tags="oval")


EnlargeShrinkCricle()
