import time
import Tkinter
from configure import Cfg
import threading
import signal
import sys

def signal_handler(singal, frame):
    print ""
    print "Ctrl+C pressed"
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


class ProtectEye(Tkinter.Tk):
    def __init__(self,parent,cfg=Cfg()):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.cfg=cfg
        self.small_break_count = 0
        self.resttime_left = 0
        self.sw = self.winfo_screenwidth()
        self.sh = self.winfo_screenheight()

        self.initialize()
        self.restClicked = False

    def initialize(self):
        self.grid()
        self.attributes("-topmost", True)
        #bind event
        self.bind("<<Destroy_Main>>", self.OnDestroyMain)

        self.labelVariable = Tkinter.StringVar()
        self.labelVariable.set("Have a rest now.")
        label = Tkinter.Label(self,textvariable=self.labelVariable,
                              anchor="w",fg="white",bg="blue")
        label.grid(column=0,row=0,columnspan=3,sticky='EW')
        
        self.buttondelay = Tkinter.Button(self,text=u"Delay",command=self.OnButtonDelay)
        self.buttondelay.grid(column=0,row=1)
        
        self.button = Tkinter.Button(self,text=u"Rest",command=self.OnButtonClick)
        self.button.grid(column=1,row=1)
        
        self.buttonQuit = Tkinter.Button(self,text=u"Quit",command=self.OnButtonQuit)
        self.buttonQuit.grid(column=2,row=1)
        
        self.grid_columnconfigure(0,weight=1)
        self.geometry("%sx%s" % (self.sw, self.sh))

    def OnDestroyMain(self,event):
        self.destroy()

    def DestroyAfterSleep(self):
        while self.resttime_left > 0:
            self.labelVariable.set("Rest %s seconds. "
                                   "Windows will disappear then."
                                   % self.resttime_left)
            self.resttime_left -= 1
            time.sleep(1)
        self.event_generate("<<Destroy_Main>>",when="tail")

    def DestroyInBackground(self):
        i = 0
        while i < self.cfg.resttime and not self.restClicked:
            time.sleep(1)
            i += 1
        if self.restClicked:
            return
        self.event_generate("<<Destroy_Main>>",when="tail")

    def OnButtonQuit(self):
        quit()

    def delaycallback(self):
        self.restClicked = True
        time.sleep(self.cfg.delayTime)
        self.geometry("%sx%s" % (self.sw, self.sh))
        self.restClicked = False
        t = threading.Thread(target=self.DestroyInBackground)
        t.daemon =True
        t.start()

    def OnButtonDelay(self):
        t = threading.Thread(target=self.delaycallback)
        t.daemon=True
        t.start()
        self.geometry("0x0")

    def OnButtonClick(self):
        self.restClicked = True
        if self.small_break_count == self.cfg.small_break_count:
            self.resttime_left = self.cfg.resttime_long
            self.small_break_count = 0
        else:
            self.resttime_left = self.cfg.resttime
            self.small_break_count += 1

        self.labelVariable.set("Rest %s seconds. "
                               "Windows will disapear then." % 
                               self.resttime_left)

        t = threading.Thread(target=self.DestroyAfterSleep)
        t.daemon=True
        t.start()
        self.button.destroy()
        self.buttondelay.destroy()

def main():
    cfg=Cfg()
    time.sleep(cfg.worktime)
    while True:
        app = ProtectEye(None)
        app.title('ProtectEye')
        t = threading.Thread(target=app.DestroyInBackground)
        t.daemon =True
        t.start()
        app.mainloop()
        time.sleep(cfg.worktime)


if __name__ == "__main__":
    main()
