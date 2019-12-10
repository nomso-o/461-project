#!/usr/bin/env python
'''
##################################################
# Wrapper for top level windows
##################################################
'''
from tkinter import *
from tkinter.messagebox import showinfo,askyesno

class _window:
    '''
    mixin share by all  windows
    '''

    foundicon = None
    iconpatt = '*.ico'
    inconmine = 'py.ico'

    def configBorders(self, app, kind, inconfile):
        if not inconfile:
            inconfile = self.foundicon
        title = app
        if kind: title += '-' + kind
        self.title(title)
        self.inconname(app)
        if inconfile:
            try:
                self.iconbitmap(inconfile)
            except:
                pass
        self.protocol('WM_DELETE_WINDOW', self.quit)
    
    def findIcon(self):
        if _window.foundicon:
            return _window.foundicon
        iconfile = None
        mymod = __import__(__name__)
        path = __name__.split('.')
        for mod in path[1:]:
            mymod = getattr( mymod, mod)
        mydir = os.path.dirname(mymod.__file__)
        myicon = os.path.join(mydir, self.inconmine)
        if os.path.exists(myicon): iconfile = myicon
        _window.foundicon = iconfile
        return iconfile

class MainWindow(Tk, _window):
    '''
    When run in main top level window
    '''
    def __init__(self, app, kind='', inconfile=None):
        Tk().__init__(self)
        self.__app = app
        self.configBorders(app, kind, inconfile)

    def quit(self):
        if self.okayToQuit():
            if askyesno(self.__app, 'Verify Quit Program'):
                self.destroy()
        else:
            showinfo(self.__app, 'Quit not allowed')
    
    def destroy(self):
        Tk.quit(self)
    
    def okayToQuit(self):
        return True
    
class PopupWindow(Toplevel, _window):
    '''
    secondary window
    '''
    def __init__(self, app, kind, inconfile):
        Toplevel.__init__(self)
        self.__app = app
        self.configBorders(app, kind, inconfile)
    
    def quit(self):
        if askyesno(self.__app, 'Verify Quit window?'):
            self.destroy()
    
    def destroy(self):
        Toplevel.destroy(self)

class QuietPopWindow(PopupWindow):
    def quit(self):
        self.destroy()

class ComponentWindow(Frame):
    '''
    To attach to other displays
    '''

    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.pack(expand=YES,fill=BOTH)
    
    def quit(self):
        showinfo('Quit', 'Not supported in attachment mode')
        





