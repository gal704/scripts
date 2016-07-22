import sys
import os
from decenc import decrypt, encrypt

v = sys.version
if "2.7" in v:
    from Tkinter import *
    import tkFileDialog
    import tkSimpleDialog
elif "3.3" in v or "3.4" in v:
    from tkinter import *
    import tkinter.tkFileDialog
    import tkinter.tkSimpleDialog

root = None
text = None
currentFile = None
password = None

def RemoveTemp():
    os.remove("temp")

def DoNothing():
    print "nothing"

def Exit():
    global root
    root.destroy()

def GetPassword():
    global password
    password = tkSimpleDialog.askstring("Password", "Enter password:")

def Open(location = None):
    global text
    global currentFile
    global password

    if "instance" in str(type(location)):
        location = None

    if location == None:
        openlocation = tkFileDialog.askopenfilenames()[0]
    else:
        openlocation = location

    if openlocation == "":
        return
    
    GetPassword()

    if not decrypt(openlocation, "temp", password):
        print "Bad password"
        RemoveTemp()
        return

    with open("temp", "r") as file1:
        data = file1.read()
    
    RemoveTemp()

    text.delete(1.0, END)
    text.insert(CURRENT, data)
    currentFile = openlocation

def SaveAs():
    savelocation = tkFileDialog.asksaveasfilename()
    if savelocation == "":
        return

    Save(savelocation)

def Save(location = None):
    global currentFile
    global text
    global password

    if "instance" in str(type(location)):
        location = None

    if location == None:
        if currentFile != None:
            location = currentFile
        else:
            SaveAs()
            return

    if password == None:
        GetPassword()

    t = text.get("1.0", "end-1c")

    with open("temp", "w+") as file1:
        file1.write(t)

    if not encrypt("temp", location, password):
        print "Bad password"
        RemoveTemp()
        return
    RemoveTemp()
    currentFile = location

def New():
    global text
    global currentFile
    global password
    password = None
    currentFile = None
    text.delete(1.0, END)

def FirstFile():
    Open(currentFile)
def main():
    global text
    global root
    global currentFile
    if len(sys.argv) == 2:
        currentFile = sys.argv[1]
    else:
        currentFile = None

    root = Tk("Text Editor")

    topMenu = Menu(root)
    fileMenu = Menu(topMenu, tearoff=0)
    fileMenu.add_command(label="New", command=New)
    fileMenu.add_command(label="Open", command=Open)
    fileMenu.add_command(label="Save", command=Save)
    fileMenu.add_command(label="Save as...", command=SaveAs)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=Exit)
    topMenu.add_cascade(label="File", menu=fileMenu)

    text = Text(root)
    
    text.bind("<Control-s>", Save)

    text.grid()
    
    root.config(menu=topMenu)
    root.after(0, FirstFile)
    root.mainloop()
    pass

if __name__ == '__main__':
    main()
