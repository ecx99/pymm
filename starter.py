from Tkinter import *
from ttk import *
import time, json,os
from subprocess import call, check_call
import re

def internet_status_ok():
    try:
        check_call(['ping' , '-n', '2', 'www.google.com'])
    except:
        return False
    return True

def doaction( cmd):
    print " ".join(['cmd', '/c'] + cmd)
    call(['cmd', '/c'] + cmd)

def getConfig():
    f=open('./config.json')
    print "Getting JSON"
    config_json = json.load(f)
    #print str(config_json)
    f.close()
    return config_json

def get_my_notes():
    print "Getting Notes"
    mt=open("/".join([my_notes_folder,my_notes_file]))
    mt_text=json.load(mt)
    mt.close()
    return mt_text['my_notes']


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.config_json=getConfig()
        self.buttons=self.config_json['buttons']
        self.grid()
        self.createWidgets()

    def do_search(self,event):
        #search_str=self.str_search.get()
        #call(['cmd','/c','start', 'chrome', 'http://google.com/?q='+search_str])
        1

    def write_my_notes(self,event):
        print "Writing Text"
        mt = open("/".join([my_notes_folder,my_notes_file]), 'w')
        my_notes = self.my_notes_box.get('1.0','end')
        my_notes_dict = {'my_notes': my_notes }
        json.dump(my_notes_dict, mt)
        mt.close()

    def redraw(self):
        config_json=getConfig()
        self.buttons=config_json['buttons']
        self.createWidgets()

    def createWidgets(self):
        idx = 0
        num_row=0

        # hard coded buttons
        Button(self, command=lambda x=["start","notepad","config.json"]: doaction(x), text=['Config'], width=20, style='TButton').grid(row=num_row, column=idx)
        idx+=1

        Button(self, command=self.quit, text=['Quit'], width=20, style=bstyle).grid(row=num_row, column=idx)
        idx+=1

        Button(self, command=self.redraw, text=['ReDraw'], width=20, style=bstyle).grid(row=num_row, column=idx)
        idx+=1

        def sort_buttons(e):
            return e['bname']

        # buttons from config
        self.buttons.sort(key=sort_buttons)
        for bs in self.buttons:

            if idx > self.config_json['max_buttons_per_row']-1:
                num_row = num_row+1
                idx=0

            print 'Button: ' + " ".join(bs['command']) +" : "+bs['bname']
            Button(self,  command=lambda x=bs['command'] : doaction(x), text=bs['bname'] 
            , width=20, style=bstyle).grid(row=num_row,column=idx)
            idx+=1

        if self.config_json['check_internet_button_on_off'] == "on":
            self.str_intstatus = StringVar()
            self.str_intstatus.set("Internet Status")
            self.btn_internet = Button(self,  command=self.set_internet_status, style=bstyle
                                       , text='Internet Status' , textvariable=self.str_intstatus)
            self.btn_internet.grid(row=num_row,column=idx)
            idx+=1


        if self.config_json['my_notes_widget_on_off'] == 'on':
            num_row+=1
            scroll = Scrollbar(self)
            self.my_notes_box = Text(self,  yscrollcommand=scroll.set)
            self.my_notes_box.insert('1.0',get_my_notes())
            self.my_notes_box.grid(row=num_row,column=0,columnspan=self.config_json['max_buttons_per_row'])
            self.my_notes_box.bind('<Key-Return>',self.write_my_notes)
            scroll.config(command = self.my_notes_box.yview)
            scroll.grid(row=num_row,column=4)

    def set_internet_status(self):
        if internet_status_ok() is False:
            self.str_intstatus.set("Internet: Down")
        else:
            self.str_intstatus.set("Internet: Online")

os.chdir(os.path.dirname(sys.argv[0]))
root = Tk()
#root.geometry("1024x768")
# root.attributes('-fullscreen', True)
myStyle = Style()
print myStyle.theme_names()
#myStyle.theme_use('clam')
root.geometry(  "-1+1" )
root.overrideredirect(1)
myConfig = getConfig()
my_notes_folder = myConfig["my_notes_folder"]
my_notes_file="my_notes.json"
myStyle.configure('TButton',font=(myConfig['font_name'], myConfig['font_size']), padding=3)
bstyle = 'TButton'
app = Application(master=root)
app.mainloop()
#root.destroy()
