from tkinter import *
import math

def leftClickButton(event):
    Weight = float(textBoxWeight.get())
    Height = float(textBoxHeight.get())
    BMI = Weight/math.pow(Height/100,2)
    print(BMI)
    labelResult.configure(text=BMI)
    if BMI >= 30.0:
        labelResult2.configure (text="Too Fat", fg="red")
    elif BMI >= 25.0 and BMI < 30:
        labelResult2.configure(text="Fat", fg="orange")
    elif BMI >= 23.0 and BMI < 25:
        labelResult2.configure(text="Chubby", fg="yellow")
    elif BMI >= 18.6 and BMI < 23:
        labelResult2.configure(text="Normal", fg="green")
    else:
        labelResult2.configure(text="To Skinny", fg="black")

MainWindow = Tk()

labelHeight = Label(MainWindow, text="ส่วนสูง (cm.)")
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0,column=1)
labelWeigth = Label(MainWindow, text="น้ำหนัก (Kg.)")
labelWeigth.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวน")
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
labelResult2 = Label(MainWindow, text="คำอธิบาย")
labelResult2.grid(row=3, column=1)

MainWindow.mainloop()