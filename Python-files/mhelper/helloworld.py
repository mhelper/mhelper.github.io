from Tkinter import *
import Tkinter, tkFileDialog

#jar cvf testing.jar plugin.yml io

name = "ComeWorld"
org_id = "io.github.mhelper"
version = "0.0.1-SNAPSHOT"

v = ""

class Application(Frame):
    def say_hi(self):
        dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Select a directory to save' + name)
        print dirname
        import os
        os.system("jar cvf " + dirname + "/" + name + "_" + version + ".jar " + name.lower() + "/plugin.yml " + name.lower() + "bin/io")
        
    

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})
        
        #------------------------------------#

        self.hi_there = Button(self)
        self.hi_there["state"] = "disabled"
        self.hi_there["text"] = "Save as jar"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack({"side": "left"})
        
        #------------------------------------#
        
        self.new = Button(self)
        self.new["state"] = "normal"
        self.new["text"] = "New plugin"
        self.new["command"] = self.new_
        self.new.pack({"side": "left"})
        
        #------------------------------------#
        
        e = Entry(self)
        e.pack()
        
        
    def new_(self):
        print "hi FOOOd is gOOd"
        self.hi_there["state"] = "normal"
        print e.get()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.title("mHelper");
root.geometry("1100x700");


app = Application(master=root)
app.mainloop()
root.destroy()
