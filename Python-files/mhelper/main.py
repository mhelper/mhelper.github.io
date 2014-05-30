# -*- coding: utf-8 -*-
from Tkinter import *
import Tkinter, tkFileDialog
import os

name_ = ""
email_ = ""
version_ = ""
dirname_ = ""

class Application(Frame):
    #something
    
    def __init__(self, master):
        #Initialize the Frame
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        
        
        
        #Create Label--------------------------------------------
        self.instruction = Label(self, text = "tf2", font=("Helvetica", 20))
        self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        #Create Label--------------------------------------------
        
        
        
        #NAME-LABEL AND INPUT------------------------------------
        self.name = Entry(self)
        self.name.grid(row = 1, column = 1, sticky = W)
        self.l1 = Label(self, text = "Plugin name:")
        self.l1.grid(row = 1, column = 0, sticky = W)
        #NAME-LABEL AND INPUT------------------------------------
        
        
        
        #O-ID LABEL AND INPUT (Organisation)---------------------
        self.oid = Entry(self)
        self.oid.grid(row =1, column = 3, sticky = W)
        self.l2 = Label(self, text = "Email(see example):")
        self.l2.grid(row = 1, column = 2, sticky = W)
        self.oid.insert(0, "com.gmail.username")
        #O-ID LABEL AND INPUT (Organisation)---------------------
        
        
        
        #VERSION LABEL AND INPUT---------------------------------
        self.ver = Entry(self,)
        self.ver.grid(row =1, column = 5, sticky = W)
        self.l3 = Label(self, text = "Version:")
        self.l3.grid(row = 1, column = 4, sticky = W)
        self.ver.insert(0, "0.0.1-SNAPSHOT")
        #VERSION LABEL AND INPUT---------------------------------
        
        
        
        #CHOOSE DIRECTORT DIALOG BUTTON--------------------------
        self.marcusknappen = Button(self, fg = "red", text = "JAG ÄR EN KNAPP", command = self.marcushej)
        self.marcusknappen.grid(row=1, column = 7, columnspan = 1, sticky = W)
        #CHOOSE DIRECTORT DIALOG BUTTON--------------------------
        
        
        
        #CREATE PLUGIN - BUTTON
        self.submit_button = Button(self, text = "New plugin", command = self.reveal)
        self.submit_button.grid(row = 1, column = 8, sticky = W)
        
        #self.text = Text(self, width = 35, height = 5, wrap = WORD)
        #self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W)
        #self.instruction = Label(self, text = "Entere the password")
        #self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        self.status = Label(self, text = "", fg="red")
        self.status.grid(row = 3, column = 0, columnspan = 2, sticky = W)
        
    def marcushej(self):
        dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Select a directory to save')
        print dirname
        
    def reveal(self):
        #Display message based on input
        name = self.name.get()
        email = self.oid.get()
        version = self.ver.get()
        
        if name != "" and email != "" and version != "":
            message = "Created plugin with no errors!"
            self.status["fg"] = "#00ff4e"
            root.geometry("1150x550")
            root.resizable(width=TRUE, height=TRUE)
            name_ = name
            email_ = email
            version_ = version
            self.submit_button["text"] = "Change info"
            
            print dirname_ + name_ 
            
        else:
            message = "You need to fill in all the fields to continue!"
            self.status["fg"] = "red"
        #self.status.delete(0.0, END)
        self.status["text"] = message

root = Tk()
root.title("mHelper")
root.geometry("1150x90")

img = PhotoImage(file='icon.gif')
root.tk.call('wm', 'iconphoto', root._w, img)

root.resizable(width=FALSE, height=FALSE)
app = Application(root)

root.mainloop()