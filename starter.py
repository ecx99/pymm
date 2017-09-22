from Tkinter import *
import time
from subprocess import call

class Application(Frame):
    def open_hulu(self):
        call ([ 'cmd','/c' 'start', 'chrome' ,"http://hulu.com/kids"])
    def open_netflix(self):
        call ([ 'cmd','/c' 'start', 'chrome' ,"http://netflix.com"])
    def open_youtube(self):
        call ([ 'cmd','/c' 'start', 'chrome' ,"http://youtube.com"])        

    def open_site(self):
        call ([ 'cmd','/c' 'start', 'chrome' ,self.site])        



    def shutdown(self):
        call ([ 'cmd','/c' 'shutdown', '/s','/f'])

    def restart(self):
        call ([ 'cmd','/c' 'shutdown', '/r','/f'])


    def createWidgets(self):

        self.p1 = Button(self, font=("Arial",self.fs,"bold"))
        self.p1["text"] = "Hulu"
        self.p1["command"] = self.open_hulu
        #self.p1["height"] = 50
        #self.p1["width"] = 30
        self.p1["bg"] = "green"
        self.p1['bd'] =10
        self.p1.pack({"side": "left"})


        self.p2 = Button(self,font=("Arial",self.fs,"bold"))
        self.p2["text"] = "Netflix"
        self.p2["command"] = self.open_netflix
        self.p2['bd'] =10
        #self.p2["height"] = 50
        #self.p2["width"] = 30
        self.p2["bg"] = "yellow"
        self.p2.pack({"side": "left"})

        self.p3= Button(self,font=("Arial",self.fs,"bold"))
        self.p3["text"] = "Youtube"
        self.p3["command"] = self.open_youtube
        self.p3['bd'] =10
        #self.p["height"] = 50
        #self.p["width"] = 30
        self.p3["bg"] = "blue"
        self.p3.pack({"side": "left"})

        self.p4 =Button(self,font=("Arial",self.fs,"bold"))
        self.p4["text"] = "Google"
        self.site = 'http://google.com'
        self.p4["command"] = self.open_site
        self.p4['bd'] =10
        #self.p["height"] = 50
        #self.p["width"] = 30
        self.p4["bg"] = "green"
        self.p4.pack({"side": "left"})        
        
        self.r0 = Button(self,font=("Arial",self.fs,"bold"))
        self.r0["text"] = "Off"
        self.r0["command"] = self.shutdown
        self.r0['bd'] =10
        #self.r0["height"] = 50
        #self.r0["width"] = 30
        self.r0["bg"] = "red"
        self.r0.pack({"side": "left"})

        self.r1 = Button(self,font=("Arial",self.fs,"bold"))
        self.r1["text"] = "Restart"
        self.r1["command"] = self.restart
        self.r1['bd'] =10
        #self.r0["height"] = 50
        #self.r0["width"] = 30
        self.r1["bg"] = "red"
        self.r1.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.site=""
        self.fs = 40
        self.pack()

        self.createWidgets()
        


root = Tk()
root.geometry("1024x768")
root.attributes('-fullscreen', True)
app = Application(master=root)
app.mainloop()
 
root.destroy()
