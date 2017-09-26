from Tkinter import *
from ttk import *
import time, json,os
from subprocess import call, check_call

def internet_status_ok():
    try:
        check_call(['ping' , '-n', '2', 'www.google.com'])

    except:
        return False

    return True

def doaction( cmd):
    call(['cmd', '/c'] + cmd)

class Application(Frame):

    def do_search(self,event):
        search_str=self.str_search.get()
        call(['cmd','/c','start', 'chrome', 'http://google.com/?q='+search_str])
        
    def createWidgets(self):
        idx = 0
        for bs in buttons:
            Button(self,  command=lambda x=bs['command'] + bs['args']: doaction(x)
                   , text=bs['bname'] ).pack()


        self.str_intstatus = StringVar()
        self.str_intstatus.set("Internet Status")
        self.btn_internet = Button(self,  command=self.set_internet_status    , text='Internet Status' , textvariable=self.str_intstatus)
        self.btn_internet.pack()


        self.str_search = StringVar()
        self.str_search.set("Search")
        self.entry_search = Entry(self, font=("Calibri", 25, "bold"),style="TButton", text='Search' , textvariable=self.str_search)
        self.entry_search.pack()

        self.entry_search.bind('<Key-Return>',
                              self.do_search)


    def set_internet_status(self):
        if internet_status_ok() is False:
            self.str_intstatus.set("Internet: Down")
        else:
            self.str_intstatus.set("Internet: Online")



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


n_bd = 10
os.chdir(os.path.dirname(sys.argv[0]))
f=open('./config.json')
buttons = json.load(f)

root = Tk()
#root.geometry("1024x768")
# root.attributes('-fullscreen', True)
style = Style()
style.configure("TButton", padding=6, relief="ridge", font=("Calibri", 25, "bold"),   background="#ccc")

app = Application(master=root)
app.mainloop()
root.destroy()
