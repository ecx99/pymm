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

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.config_json=getConfig()
        self.myStyle = Style()
        self.myStyle.configure('TButton',font=(self.config_json['font_name'], self.config_json['font_size']))
        self.myStyle.configure('TText',font=(self.config_json['font_name'], self.config_json['font_size']))
        self.buttons=self.config_json['buttons']
        self.grid()
        self.createWidgets()

    def do_search(self,event):
        #search_str=self.str_search.get()
        #call(['cmd','/c','start', 'chrome', 'http://google.com/?q='+search_str])
        1

    def get_my_notes(self):
        print "Getting Notes"
        mt=open("/".join([self.config_json['my_notes_folder'],my_notes_file]))
        mt_text=json.load(mt)
        mt.close()
        return mt_text['my_notes']

    def write_my_notes(self,event):
        print "Writing Text"
        mt = open("/".join([self.config_json['my_notes_folder'],my_notes_file]), 'w')
        my_notes = self.my_notes_box.get('1.0','end')
        my_notes_dict = {'my_notes': my_notes }
        json.dump(my_notes_dict, mt)
        mt.close()

    def redraw(self):
        self.config_json=getConfig()
        self.buttons=self.config_json['buttons']
        self.myStyle.configure('TButton',font=(self.config_json['font_name'], self.config_json['font_size']))
        self.createWidgets()

    def createWidgets(self):
        idx = 0
        row_num=0

        # hard coded buttons
        Button(self, command=lambda x=["start","notepad","config.json"]: doaction(x), text=['Config'], width=self.config_json['button_width']).grid(row=row_num, column=idx)
        idx+=1

        Button(self, command=self.quit, text=['Quit'], width=self.config_json['button_width']).grid(row=row_num, column=idx)
        idx+=1

        Button(self, command=self.redraw, text=['ReDraw'], width=self.config_json['button_width']).grid(row=row_num, column=idx)
        idx+=1

        if self.config_json['check_internet_button_on_off'] == "on":
            self.str_intstatus = StringVar()
            self.str_intstatus.set("Internet Status")
            self.btn_internet = Button(self,  command=self.set_internet_status
                                       ,  textvariable=self.str_intstatus,width=self.config_json['button_width'])
            self.btn_internet.grid(row=row_num,column=idx)
            idx+=1

        def sort_buttons(e):
            return e['bname']

        # buttons from config
        self.buttons.sort(key=sort_buttons)
        for bs in self.buttons:

            if idx > self.config_json['max_buttons_per_row']-1:
                row_num = row_num+1
                idx=0

            print 'Button: ' + " ".join(bs['command']) +" : "+bs['bname']
            Button(self,  command=lambda x=bs['command'] : doaction(x), text=bs['bname'] 
            , width=self.config_json['button_width']).grid(row=row_num,column=idx)
            idx+=1



        if self.config_json['my_notes_widget_on_off'] == 'on':
            row_num+=1
            self.scroll = Scrollbar(self)
            
            self.my_notes_box = Text(self,  yscrollcommand=self.scroll.set,width=45,relief='sunken',font=(self.config_json['font_name'], self.config_json['font_size']))
            self.my_notes_box.insert('1.0',self.get_my_notes())
            self.my_notes_box.bind('<Key-Return>',self.write_my_notes)
            self.my_notes_box.grid(row=row_num,column=0,columnspan=self.config_json['max_buttons_per_row']-1,sticky='w')
            self.scroll.grid(row=row_num,column=self.config_json['max_buttons_per_row']-1,sticky='w')
            self.scroll.config(command = self.my_notes_box.yview)
            

    def set_internet_status(self):
        if internet_status_ok() is False:
            self.str_intstatus.set("Internet: Down")
        else:
            self.str_intstatus.set("Internet: Online")

os.chdir(os.path.dirname(sys.argv[0]))
root = Tk()
#root.geometry("1024x768")
# root.attributes('-fullscreen', True)

#myStyle.theme_use('clam')
root.geometry(  "-1+1" )
root.overrideredirect(1)
my_notes_file="my_notes.json"
app = Application(master=root)
app.mainloop()
print "EXITING"
#root.destroy()
