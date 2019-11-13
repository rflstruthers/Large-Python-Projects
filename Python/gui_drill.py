# Python Ver:   3.7.4
#
# Author:       Reilly Struthers
#
# Purpose:      Create GUI using grid grometry.
#
# Tested OS:  This code was written and tested to work with Windows 10.


from tkinter import * # import tkinter module
import tkinter as tk

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # create window (size, title)
        self.master = master
        self.master.minsize(440,155)
        self.master.maxsize(440,155)
        self.master.title('Check files')

        # buttons
        self.btn_browse1 = tk.Button(self.master, width=12, height=1, text='Browse...')
        self.btn_browse1.grid(row=0,column=0,padx=(10,10),pady=(30,5),sticky=W)
        self.btn_browse2 = tk.Button(self.master, width=12, height=1, text='Browse...')
        self.btn_browse2.grid(row=1,column=0,padx=(10,10),pady=(5,5),sticky=W)
        self.btn_check_files = tk.Button(self.master, width=12, height=2, text='Check for files')
        self.btn_check_files.grid(row=2,column=0,padx=(10,10),pady=(5,0),sticky=W)
        self.btn_close = tk.Button(self.master, width=12, height=2, text='Close program')
        self.btn_close.grid(row=2,column=2,padx=(10,10),pady=(5,0),sticky=E)

        # entries
        self.txt_entry1 = tk.Entry(self.master, width=50, text='')
        self.txt_entry1.grid(row=0,column=1,columnspan=2,padx=(10,10),pady=(30,5),sticky=E)
        self.txt_entry2 = tk.Entry(self.master, width=50, text='')
        self.txt_entry2.grid(row=1,column=1,columnspan=2,padx=(10,10),pady=(5,5),sticky=E)
        

        


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
