# Python Ver:   3.7.4
#
# Author:       Reilly Struthers
#
# Purpose:      Create GUI that accesses directories and returns directory path.
#
# Tested OS:  This code was written and tested to work with Windows 10.

import os
from tkinter import * # import tkinter module
import tkinter as tk
from tkinter import filedialog 

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # create window (size, title)
        self.master = master
        self.master.minsize(440,155)
        self.master.maxsize(440,155)
        self.master.title('Browse directories')

        # labels
        self.lbl_selected = tk.Label(self.master,text='Directory path:')
        self.lbl_selected.grid(row=0,column=0,padx=(10,0),pady=(30,5),sticky=N+W)

        # button (calls on 'openDir' function when clicked)
        self.btn_browse1 = tk.Button(self.master, width=12, height=1, text='Browse...', command=lambda: openDir(self))
        self.btn_browse1.grid(row=1,column=0,padx=(10,10),pady=(10,5),sticky=S+W)

        # entries
        self.txt_entry1 = tk.Entry(self.master, width=50, text='')
        self.txt_entry1.grid(row=0,column=1,columnspan=2,padx=(0,10),pady=(30,5),sticky=E)

        # function is called when button is clicked, opens window and has user select a directory
        def openDir(self):
            root = tk.Tk()
            root.withdraw()
            dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
            if len(dirname ) > 0: # if a directory is selected, it is printed in 'txt_entry1'
                path_name = os.path.abspath(dirname) # gets absolute directory path
                self.txt_entry1.delete(0,END) # clears any previous text in 'txt_entry1'
                self.txt_entry1.insert(END, path_name) # prints 'path_name' in 'txt_entry1'















if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
