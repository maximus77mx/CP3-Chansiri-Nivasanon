from tkinter import *
import math
def leftcilckButton(event):
    print(float(textboxWeight.get())/math.pow(float(textboxHeight.get()),2))

MainWindow = Tk()
lableHeight = Label(MainWindow,text="ส่วนสูง (cm.)")
lableHeight.grid(row=0,column=0)
textboxHeight = Entry(MainWindow)
textboxHeight.grid(row=0,column=1)
lableWeight = Label(MainWindow,text="น้ำหนัก (kg.)")
lableWeight.grid(row=1,column=0)
textboxWeight = Entry(MainWindow)
textboxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>',leftcilckButton)
calculateButton.grid(row=2)
MainWindow.mainloop()