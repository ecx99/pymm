from Tkinter import *
import time
from subprocess import call

class Application(Frame):

    def doaction(self,cmd):
        call ([ 'cmd','/c' ] + cmd ) 

    def createWidgets(self):
        idx=0
        for bs in buttons:
            
            Button(self, command=lambda x = bs['command'] + bs['args']: self.doaction(x), font=bs['font']
                             , text=bs['bname'],bg=bs['bg'] ,bd = bs['bd'] ).pack(bs['pack'] )

        intstatus = Button(self, command='', font=bs['font']
                             , text='intstatus',bg='green' ,bd = 10 ).pack(bs['pack'] )

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

n_bd=10
htp = 'http://'
font=("Arial",25,"bold")
start='start'
chrome = 'chrome'
buttons =[
   { 'bname' : 'Hulu' , 'args' : [htp+'hulu.com/kids'],  'command' : [start,chrome] , 'bg' : 'green', 'bd' : n_bd, 'pack' : { 'side' : 'left' } ,'font' : font}
  ,{ 'bname' : 'Youtube' , 'args' : [htp+'youtube.com'], 'command' : [start,chrome] , 'bg' : 'blue', 'bd' : n_bd, 'pack' : { 'side' : 'left' },'font' : font }
  ,{ 'bname' : 'Netflix' , 'args' : [ htp+'netflix.com'] , 'command' : [start,chrome] , 'bg' : 'orange', 'bd' : n_bd, 'pack' : { 'side' : 'left' } ,'font' : font}
  ,{ 'bname' : 'Google' , 'args' : [ htp+'google.com' ] ,  'command' : [start,chrome]
        ,  'bg' : 'green', 'bd' : n_bd, 'pack' : { 'side' : 'left' } ,'font' : font}
  ,{ 'bname' : 'Weather' , 'args' : [ htp+'weather.com/weather/today/l/21042:4:US' ] , 'command' : [start,chrome],  'bg' : 'yellow', 'bd' : n_bd, 'pack' : { 'side' : 'left' } ,'font' : font}
  ,{ 'bname' : 'Off' , 'args' : ['/s','/f'],'command' :  ['shutdown'], 'bg' : 'red', 'bd' : n_bd, 'pack' : { 'side' : 'left' } ,'font' : font}
  ,{ 'bname' : 'Restart' , 'args' : ['/r','/f'], 'command' : ['shutdown'] , 'bg' : 'red', 'bd' : n_bd, 'pack' : { 'side' : 'left' }
       ,'font' : font}
 ]

root = Tk()
#root.geometry("1024x768")
#root.attributes('-fullscreen', True)
app = Application(master=root)
app.mainloop()
root.destroy()
