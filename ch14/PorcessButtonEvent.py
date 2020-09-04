from tkinter import *

def processOK():
    print("OK 버튼이 클릭되었습니다.")

def processCancel():
    print("Cancel 버튼이 클릭되었습니다.")

window = Tk()

buttonOK = Button(window, text="OK", fg="red", command = processOK)
buttonCancel = Button(window, text="Cancel", fg="yellow", command = processCancel)

buttonOK.pack()
buttonCancel.pack()

window.mainloop()
