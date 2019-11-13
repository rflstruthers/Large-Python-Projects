
import tkinter
from tkinter import * # import all widgits from Tkinter

# Frame is parent class of Tkinter
class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        # create Tkinter window:
        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Learning Tkinter')
        self.master.config(bg='lightgrey')

        # create variables for first and last names
        self.varFName = StringVar()
        self.varLName = StringVar()

        # create labels for FName and Lname text boxes
        self.lblFName = Label(self.master,text='First Name: ',font=('Helvetica',16),fg='black',bg='lightgrey')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))

        self.lblLName = Label(self.master,text='Last Name: ',font=('Helvetica',16),fg='black',bg='lightgrey')
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        # create label for output of user input
        self.lblDisplay = Label(self.master,text='',font=('Helvetica',16),fg='black',bg='lightgrey')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        # create entry box in 'master' window for first name
        self.txtFName = Entry(self.master,text=self.varFName,font=('Helvetica',16),fg='black',bg='lightblue')
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        # create entry box in 'master' window for last name
        self.txtLName = Entry(self.master,text=self.varLName,font=('Helvetica',16),fg='black',bg='lightblue')
        self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))

        # create buttons, 'command' calls fxn when button is clicked
        self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)

        self.btnCancel = Button(self.master, text='Cancel', width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)

    # fxns that are called when buttons are clicked
    def submit(self):
        fn = self.varFName.get() # stores user input as 'fn'
        ln = self.varLName.get() # stores user input as 'ln'
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln)) # prints 'fn' and 'ln' to 'lblDisplay'

    def cancel(self):
        self.master.destroy()
        

if __name__ == '__main__':
    root = Tk() # assigns 'Tkinter' class to 'root' variable
    App = ParentWindow(root) # assigns 'ParentWindow' class to 'App' variable
    root.mainloop() # makes program stay open until main loop is closed
    
