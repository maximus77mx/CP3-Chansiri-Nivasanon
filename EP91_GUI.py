from tkinter import *

def sayHelloWorld():
   print("Hello World")

MainWindow = Tk()
lable = Label(MainWindow,text = "Hello World",width =20,fg = "#F5DF4D",bg="#939597",font=("Century Gothic",38),anchor=W).grid(row=0,column=1)
MainWindow.mainloop()


'''
button = Button(MainWindow,text = "Click me1",command = sayHelloWorld).grid(row=2,column=1)
button2 = Button(MainWindow,text = "Click me2",command = sayHelloWorld).grid(row=1,column=1)
button3 = Button(MainWindow,text = "Click me3",command = sayHelloWorld).grid(row=0,column=2)
'''
