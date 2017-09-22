from Tkinter import *
from ttk import *
import time
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


    def createWidgets(self):
        idx = 0
        for bs in buttons:
            Button(self,  command=lambda x=bs['command'] + bs['args']: doaction(x)
                   , text=bs['bname'] ).pack()


        self.str_intstatus = StringVar()
        self.str_intstatus.set("Internet Status")
        self.btn_internet = Button(self,  command=self.set_internet_status    , text='Internet Status' , textvariable=self.str_intstatus)
        self.btn_internet.pack()

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
htp = 'http://'
font = ("Arial", 25, "bold")
start = 'start'
chrome = 'chrome'
buttons = [
    {'bname': 'Hulu', 'args': [htp + 'hulu.com/kids'], 'command': [start, chrome], 'bg': 'green', 'bd': n_bd,
     'pack': {'side': 'left'}, 'font': font}
    , {'bname': 'Youtube', 'args': [htp + 'youtube.com'], 'command': [start, chrome], 'bg': 'blue', 'bd': n_bd,
       'pack': {'side': 'left'}, 'font': font}
    , {'bname': 'Netflix', 'args': [htp + 'netflix.com'], 'command': [start, chrome], 'bg': 'orange', 'bd': n_bd,
       'pack': {'side': 'left'}, 'font': font}
    , {'bname': 'Google', 'args': [htp + 'google.com'], 'command': [start, chrome], 'bg': 'green', 'bd': n_bd,
       'pack': {'side': 'left'}, 'font': font}
    , {'bname': 'Weather', 'args': [htp + 'weather.com/weather/today/l/21042:4:US'], 'command': [start, chrome],
       'bg': 'yellow', 'bd': n_bd, 'pack': {'side': 'left'}, 'font': font}
    , {'bname': 'Off', 'args': ['/s', '/f'], 'command': ['shutdown'], 'bg': 'red', 'bd': n_bd, 'pack': {'side': 'left'},
       'font': font}
    , {'bname': 'Restart', 'args': ['/r', '/f'], 'command': ['shutdown'], 'bg': 'red', 'bd': n_bd,
       'pack': {'side': 'left'}, 'font': font}
]

root = Tk()
#root.geometry("1024x768")
# root.attributes('-fullscreen', True)
style = Style()
style.configure("TButton", padding=6, relief="flat", font=("Calibri", 25, "bold"),   background="#ccc")

app = Application(master=root)
app.mainloop()
root.destroy()
