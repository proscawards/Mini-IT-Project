from tkinter import *
from tkinter import ttk
if sys.version[0] == '2':
    import Tkinter as tk
else:
    import tkinter as tk

	
class Endscreen:

    def __init__(self):
        global root
        root = Toplevel()    
        root.title("Long Distance Bus Booking System")
        root.resizable(0,0)
        root.attributes("-toolwindow",1)
        root.protocol('WM_DELETE_WINDOW')
        # Canvas Size
        w = 500
        h = 400
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        # calculate position x and y coordinates
        x = (sw/2) - (w/2)
        y = (sh/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.iconbitmap('busicon32.ico')
        root.bind("<Button-1>", self.leftclick)
        root.bind("<Button-2>", self.middleclick)
        root.bind("<Button-3>", self.rightclick)
        self.display()
        self.exitdisplay()
        root.mainloop()

    def display(self):
        endimg = PhotoImage(file = 'endscreendis.png')
        enddisplay = Label(root, image = endimg)
        enddisplay.image = endimg
        enddisplay.place(x=120, y=130)
	
    def exitdisplay(self):
        exitdisplay = Label(root, text = "Click anywhere to exit the program.")
        exitdisplay.place(x = 163, y = 155)

    def leftclick(self, event):
        exit()
	
    def middleclick(self, event):
        exit()

    def rightclick(self, event):
        exit()

if __name__ == '__main__':
	end = Endscreen()



    

