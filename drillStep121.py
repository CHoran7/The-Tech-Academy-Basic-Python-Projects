import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.geometry('{}x{}'.format(400,200))#set window size
        self.master.title('Check files')#title that appears at the top of window

        self.varFName1 = StringVar()
        self.varFName2 = StringVar()

        #Creating the buttons and entries
        self.btnBrowse1 = Button(self.master, text="Browse...", width=15, height=1)
        self.btnBrowse1.grid(row=0, column=0, padx=(10,0), pady=(50,0))

        self.btnBrowse2 = Button(self.master, text="Browse...", width=15, height=1)
        self.btnBrowse2.grid(row=1, column=0, padx=(10,0), pady=(10,0))

        self.btnCheck = Button(self.master, text="Check for files...", width=15, height=2)
        self.btnCheck.grid(row=2, column=0, padx=(10,0), pady=(10,0))

        self.btnClose = Button(self.master, text="Close Program", width=15, height=2)
        self.btnClose.grid(row=2, column=2, columnspan=1, padx=(150,0), pady=(10,0))

        self.txtFName1 = Entry(self.master,text=self.varFName1,font=("Helvetica", 16), fg='black', bg='white')
        self.txtFName1.grid(row=0, column=1, columnspan=2, padx=(20,0), pady=(50,0))

        self.txtFName2 = Entry(self.master,text=self.varFName2,font=("Helvetica", 16), fg='black', bg='white')
        self.txtFName2.grid(row=1, column=1, columnspan=2, padx=(20,0), pady=(10,0))

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
