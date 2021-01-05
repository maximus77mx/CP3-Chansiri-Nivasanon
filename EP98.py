from tkinter import *
def leftcilckButton(event):
    print("Left Click")
def doubleClickButoon(event):
    print("Double Click")

main =Tk()
button = Button(main, text = "my Buttom!!")
button.pack()
button.bind('<Button-1>', leftcilckButton)
button.bind('<Double-1>', doubleClickButoon)
main.mainloop()
