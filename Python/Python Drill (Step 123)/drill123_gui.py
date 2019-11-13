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
import os

# import function and main modules
import drill123_fxn
import drill123_main

# creates GUI
def load_gui(self):
    # browse buttons open window that allows user to search for source and destination directories
    self.btn_browse1 = tk.Button(self.master, width=22, height=1, text='Browse source...', command=lambda: drill123_fxn.openDir1(self))
    self.btn_browse1.grid(row=0,column=0,padx=(10,10),pady=(30,5),sticky=W)
    self.btn_browse2 = tk.Button(self.master, width=22, height=1, text='Browse destination...', command=lambda: drill123_fxn.openDir2(self))
    self.btn_browse2.grid(row=1,column=0,padx=(10,10),pady=(5,5),sticky=W)
    # check files button searches source dir for .txt files
    self.btn_check_files = tk.Button(self.master, width=22, height=2, text='Move text files', command=lambda: drill123_fxn.dot_txt(self))
    self.btn_check_files.grid(row=2,column=0,padx=(10,10),pady=(5,0),sticky=W)
    # closes the program
    self.btn_close = tk.Button(self.master, width=12, height=2, text='Close program', command=lambda: drill123_fxn.quit(self))
    self.btn_close.grid(row=2,column=2,padx=(10,10),pady=(5,0),sticky=E)

    # entries
    self.txt_entry1 = tk.Entry(self.master, width=50, text='')
    self.txt_entry1.grid(row=0,column=1,columnspan=2,padx=(10,10),pady=(30,5),sticky=E)
    self.txt_entry2 = tk.Entry(self.master, width=50, text='')
    self.txt_entry2.grid(row=1,column=1,columnspan=2,padx=(10,10),pady=(5,5),sticky=E)
        

        


if __name__ == "__main__":
    pass
