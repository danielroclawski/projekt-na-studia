from tkinter import *

top = Tk()
C = Canvas(top, bg="blue", height=1250, width=1300)
filename = PhotoImage(file = "C:\\Users\\Daniel\\Downloads\\asd.png")
background_label = Label(top, image = filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()
C.mainloop()


