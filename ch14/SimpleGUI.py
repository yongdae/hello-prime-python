from tkinter import *

window = Tk()

label = Label(window, text="파이썬에 오신 것을 환영합니다.")
button = Button(window, text="저를 클릭해주세요.")

label.pack()
button.pack()

window.mainloop()
