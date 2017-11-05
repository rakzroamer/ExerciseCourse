from tkinter import *

root = Tk()
theLabel = Label(root, text="This is my first gui")

topframe = Frame(root)
topframe.pack()
bottomframe = Frame(root)
bottomframe.pack(side=BOTTOM)
#theLabel.pack()
root.mainloop()
