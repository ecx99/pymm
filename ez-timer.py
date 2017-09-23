from Tkinter import *
import time
class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def seturl(self,url):
        self.url = seturl.url

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "Quit"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.time_entry = Entry()
        self.time_entry.pack()
        self.contents = StringVar()
        self.time_entry ["textvariable"] = self.contents


        self.display_entry = Entry()
        self.display_entry.pack()
        self.display = StringVar()
        self.display_entry ["textvariable"] = self.display
        self.display.set("0")

        self.display_entry.bind('<Key-Return>',
                              self.set_stop_seconds)

        


        self.countdown_label= Label()
        self.countdown = StringVar()
        self.countdown_label["textvariable"] = self.countdown
        self.countdown.set(0)
        self.countdown_label.pack()
        
        self.set_contents()


    def print_contents(self, event):
        print "hi. contents of entry is now ---->", \
              self.contents.get()

    def set_stop_seconds(self,event):
        print "stop-"
        self.stop_seconds=int(self.display.get())
        self.current_seconds=0
        self.countdown_label["bg"] = "white"

    def set_contents(self):
        print "set"
        self.contents.set(time.strftime("%H:%M:%S"))
        self.current_seconds = self.current_seconds+1
        if self.stop_seconds > 0:
            
            print self.current_seconds,self.stop_seconds
            self.countdown.set(self.stop_seconds-self.current_seconds)
            if self.current_seconds > self.stop_seconds:
                #self.QUIT["bg"]   = "black"
                self.countdown_label["bg"] = "red"
                self.current_seconds=0
                self.stop_seconds=5
                #self.display.set(0)
                self.countdown.set(0)

        root.after(1000,self.set_contents)


    def __init__(self, master=None):
        self.stop_seconds=5
        self.current_seconds=0
        Frame.__init__(self, master)
        self.pack()
        self.url=""

        self.createWidgets()
        


root = Tk()
app = Application(master=root)
app.mainloop()
 
root.destroy()
