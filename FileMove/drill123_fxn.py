# Python Ver:   3.7.4
#
# Author:       Reilly Struthers
#
# Purpose:      Python course drill. Create GUI that acesses a directory, checks
#               for .txt files, moves them to a different directory, and adds
#               the moved files to a database.
#
# Tested OS:  This code was written and tested to work with Windows 10.

import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import time
import shutil
import sqlite3

# import GUI and main modules
import drill123_main
import drill123_gui

# function is called when button is clicked, opens window and has user select a directory
def openDir1(self):
    root = tk.Tk()
    root.withdraw()
    dirname1 = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    if len(dirname1) > 0: # if a directory is selected, it is printed in 'txt_entry1'
        path_name1 = os.path.abspath(dirname1) # gets absolute directory path
        self.txt_entry1.delete(0,END) # clears any previous text in 'txt_entry1'
        self.txt_entry1.insert(END, path_name1) # prints 'path_name1' in 'txt_entry1'

def openDir2(self):
    root = tk.Tk()
    root.withdraw()
    dirname2 = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    if len(dirname2) > 0: # if a directory is selected, it is printed in 'txt_entry2'
        path_name2 = os.path.abspath(dirname2) # gets absolute directory path
        self.txt_entry2.delete(0,END) # clears any previous text in 'txt_entry2'
        self.txt_entry2.insert(END, path_name2) # prints 'path_name2' in 'txt_entry2'

# checks for .txt files in source directory, moves them to destination directory, records files moved in database
def dot_txt(self):
    path_source = self.txt_entry1.get() # gets source directory path from 'txt_entry1'
    path_dest = self.txt_entry2.get() # destination directory
    
    if len(path_source) and len(path_dest) > 0:
        if path_source == path_dest:
            messagebox.showerror("Duplicate directory","Please select unique source and destination directories.")
        else:
            files = os.listdir(path_source) # list of files in directory that user selected as source directory
            txtFiles = [] # creates dictionary of files in source directory
            file_time = []
            
            for names in files: # iterates through source directory looking for .txt files
                if names.endswith(".txt"):
                    
                    txtPath = os.path.join(path_source,names)
                    shutil.move(txtPath,path_dest) # move files from source to destination
                    txtPath_new = os.path.join(path_dest,names)
                    
                    t = os.path.getmtime(txtPath_new) # get time-stamp
                    tStamp = modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t)) # change time-stamp format
                    txtFiles.append(names) # add file name and corresponding time-stamp to dictionary
                    file_time.append(tStamp)
                    
            if len(txtFiles) > 0:
                create_db(txtFiles,file_time)
                messagebox.showinfo("Files moved","Text files sucessfully moved.")
            else:
                messagebox.showerror("Missing files","There are no text files in source directory. \nPlease select a different source directory.")
    else:
        messagebox.showerror("Missing directory","Please select a source and destination directory.")
        
def create_db(txtFiles,file_time): # create db and table and column, call on addToDb()
    conn = sqlite3.connect('db_drill123.db')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS tbl_txtFiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_text_files TEXT UNIQUE, \
            col_time_stamp TEXT)')
        conn.commit()
    conn.close()
    addToDb(txtFiles,file_time)

def addToDb(txtFiles,file_time): # add list of .txt files to table in db
    conn = sqlite3.connect('db_drill123.db')
    with conn:
        cur = conn.cursor()
        # add data to each column
        for i in range(len(txtFiles)):
            cur.execute('INSERT OR IGNORE INTO tbl_txtFiles (col_text_files, col_time_stamp) VALUES (?,?)', (txtFiles[i], file_time[i]))
    conn.close()
    display_txt()

def display_txt(): # select text files from table and print them
    conn = sqlite3.connect('db_drill123.db')
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT col_text_files, col_time_stamp FROM tbl_txtFiles')
        txt = cur.fetchall() # get everything from cur
        
        print('The Text files are: \n')
        
        for i in txt:
            print(i, sep = "\n") 
    conn.close()
    
        
# this closes app
def quit(self):
    self.master.destroy()
    os._exit(0)
    


if __name__ == "__main__":
    pass
