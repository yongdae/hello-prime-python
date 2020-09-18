from tkinter import *


class ImageDemoSample:
    def __init__(self):
        window = Tk()
        window.title("이미지 데모")

        koImage = PhotoImage(file="image/korea.gif")
        ukImage = PhotoImage(file="image/uiIcon.gif")
        crossImage = PhotoImage(file="image/x.gif")
        circleImage = PhotoImage(file="image/o.gif")

        frame = Frame(window)
        frame.pack()

        Checkbutton(frame, image=koImage).pack(side=LEFT)
        Checkbutton(frame, image=ukImage).pack(side=LEFT)
        Radiobutton(frame, image=crossImage).pack(side=LEFT)
        Radiobutton(frame, image=circleImage).pack(side=LEFT)

        window.mainloop()


ImageDemoSample()
