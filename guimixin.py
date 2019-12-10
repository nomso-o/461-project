#!/usr/bin/env python
'''
####################################################################
a "mixin" class for other frames: common methods for canned dialogs,
spawing programs, simple text viewers, etc; this class must be mixed
which a Frame (or a subclass derived from Frame) for it's quit method
######################################################################
'''
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from scrolledtext import ScrolledText

class GuiMixin:
    def infobox(self,title,text,*args):
        return showinfo(title,text)

    def errorbox(self,text):
        showerror('Error!',text)
    
    def question(self,title, text, *args):
        return askyesno(title, text)
    
    def notdone(self):
        showerror('Not implemented', 'Option not available')
    
    def quit(self):
        ans = self.question('Verify quit', 'Are you sure you want to quit?')
        if ans:
            Frame.quit(self)
    
    def help(self):
        self.infobox('Help','This feature is not available as of now')
    
    def selectOpenFile(self, file="", dir="."):
        return askopenfilename(initialdir=dir,initialfile=file)
    
    def selectSaveFile(self, file="", dir="."):
        return asksaveasfilename(initialfile=file,initialdir=dir)
    
    def clone(self,args=()):
        new = Toplevel()
        myclass = self.__class__
        myclass(new, *args)
    
    def browser(self, filename=None):
        if not filename:
           filename =  self.selectOpenFile()
        new = Toplevel()
        view = ScrolledText(parent=new,file=filename)
        view.text.config(height=30, width=85)
        view.text.config(font=('courier', 10, 'normal'))
        new.title('Text viewer')
    
if __name__ == '__main__':

    class TestMixin(GuiMixin, Frame):
        def __init__(self, parent=None):
            Frame.__init__(self,parent)
            self.pack()
            self.config(width=100)
            import widgets
            widgets.button(self,text='quit', command=self.quit)
            widgets.button(self,text='help', command=self.help)
            widgets.button(self,text='clone', command=self.clone)
            widgets.button(self,text='browse', command=self.browser)
            
    
    TestMixin().mainloop()