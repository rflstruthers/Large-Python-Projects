# Python Ver:   3.7.4
#
# Author:       Reilly Struthers
#
# Purpose:      Python course drill. Create GUI that acesses a directory, checks
#               for .txt files, moves them to a different directory, and adds
#               the moved files to a database.
#
# Tested OS:  This code was written and tested to work with Windows 10.


from tkinter import *
import tkinter as tk

# import function and gui modules
import drill123_fxn
import drill123_gui

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # create window (size, title)
        self.master = master
        self.master.minsize(510,155)
        self.master.maxsize(510,155)
        self.master.title('Move files')

        # load the GUI widgets from a separate module
        drill123_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
