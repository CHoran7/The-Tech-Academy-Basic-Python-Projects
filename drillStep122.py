import tkinter
from tkinter import *
from tkinter import filedialog

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.geometry('{}x{}'.format(400,200))#set window size
        self.master.title('Find files')#title that appears at the top of window

        #Creating the buttons and entries
        self.btnBrowse1 = Button(self.master, text="Browse...", width=15, height=1, command=lambda: browseDirectory(self))
        self.btnBrowse1.grid(row=0, column=0, padx=(10,0), pady=(50,0))

        self.txtFName1 = Entry(self.master,text='',font=("Helvetica", 16), fg='black', bg='white')
        self.txtFName1.grid(row=0, column=1, columnspan=2, padx=(20,0), pady=(50,0))

def browseDirectory(self):
    self.txtFName1.delete(0,END)
    dirname = filedialog.askdirectory(title='Please select a directory')
    print(dirname)
    self.txtFName1.insert(0,dirname)

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
