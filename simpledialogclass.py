#!/usr/bin/env python
'''
##################################
Custom Dialog template
##################################
'''

from  tkinter import *
class MyDialog(Toplevel):
    def __init__(self, parent, title=None):
        Toplevel.__init__(self)
        if title:
            self.title
        
        self.parent = parent
        self.result = None

        body = Frame(self)
        self.initial_focus = self.body(body)
        self.buttonbox()
        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self
        
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,parent.winfo_rootx()+50))
        self.initial_focus.focus_set()
        self.wait_window(self)

    def body(self,master):
        ###create dialog body
        pass
    def buttonbox(self):
        ### add standard button box.

        box = Frame(self)

        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text='Cancel', width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind('<Return>', self.ok)
        self.bind('<Escape>', self.cancel)

    def ok(self,event=None):
        if not self.validate():
            self.initial_focus.focus_set()
            return 
        
        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()
    def cancel (self, event=None):
        self.parent.focus_set()
        self.destroy()

    def validate(self):
        return 1
    
    def apply(self):
        pass
    
    
if __name__ == '__main__':
    class Dialog(MyDialog):
        def body(self, master):
            Label(master, text='First:').grid(row=0)
            Label(master, text='Second:').grid(row=1)
            self.e1 = Entry(master)
            self.e2 = Entry(master)
            return self.e1

        def apply(self):
            first = int(self.e1.get())
            second = int(self.e2.get())
            print(first,second)
    root = Tk()
    Dialog(root)
    root.mainloop()
