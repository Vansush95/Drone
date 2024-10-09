import tkinter as tk
import os
from tkinter import *
import subprocess

root = tk.Tk()

# Tkinter widgets needed for scrolling.  The only native scrollable container that Tkinter provides is a canvas.
# A Frame is needed inside the Canvas so that widgets can be added to the Frame and the Canvas makes it scrollable.
cTableContainer = tk.Canvas(root)
fTable = tk.Frame(cTableContainer)
sbVerticalScrollBar = tk.Scrollbar(root)

clicked = StringVar()
clicked.set("Lynis")
drop = OptionMenu(root, clicked, "Lynis" ,"Chkrootkit")
drop.pack()

def runApp():
	if clicked == "Lynis" :
		createScrollableContainer()
		Outputfileobject = os.popen('lynis audit system')
		Output = Outputfileobject.read()
		Outputfileobject.close()
		tk.mylabel = Label(fTable, text=Output).grid()
		updateScrollRegion()
	else :
		createScrollableContainer()
		Outputfileobject = os.popen('sudo chkrootkit')
		Output = Outputfileobject.read()
		Outputfileobject.close()
		tk.mylabel = Label(fTable, text=Output).grid()
		updateScrollRegion()


dropButt = Button(root, text="SCAN" , command = runApp).pack()

def updateScrollRegion():
	cTableContainer.update_idletasks()
	cTableContainer.config(scrollregion=fTable.bbox())

# Sets up the Canvas, Frame, and scrollbars for scrolling
def createScrollableContainer():
	cTableContainer.config(yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
	sbVerticalScrollBar.config(orient=tk.VERTICAL, command=cTableContainer.yview)

	sbVerticalScrollBar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
	cTableContainer.pack(fill=tk.BOTH, side=tk.LEFT, expand=tk.TRUE)
	cTableContainer.create_window(0, 0, window=fTable, anchor=tk.NW)

v = StringVar(root, value='command name')
cmd = Entry(root,textvariable = v)
cmd.pack()

def onClick():
	createScrollableContainer()
	Outputfileobject = subprocess.Popen(cmd.get(),shell= True,stdout=subprocess.PIPE)  # cmd.get is to get the string value we entered in the entry widget
	Outputfileobject.wait()
	Output = Outputfileobject.stdout.readlines()
	for i in Output:
		tk.mylabel = Label(fTable, text = i).grid()
		updateScrollRegion()

def ClearS() :
	for widget in fTable.winfo_children():
		widget.destroy()

myButton = Button(root, text="Enter", command=onClick)
myButton.pack()
DelButton = Button(root, text="clear", command=ClearS)
DelButton.pack()


root.mainloop()
