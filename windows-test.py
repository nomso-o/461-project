#!/usr/bin/env python
'''
######################################
windows self test
######################################
'''
from tkinter import *
from windows import MainWindow, PopupWindow, ComponentWindow
def _selftest():
    #mixin usage

    class content:
        def __init__(self):
            Button(self, text='Larch', command=self.quit).pack()
            Button(self, text='Sing', command=self.destroy).pack()
    class contentmix(MainWindow, content):
        def __init__(self):
            MainWindow.__init__(self,'Mixin','Main')
            content.__init__(self)
    contentmix()
    class contentmix(PopupWindow, content):
        def __init__(self):
            PopupWindow.__init__(self,'Mixin','Main')
            content.__init__(self)
    prev = contentmix()
    class contentmix(ComponentWindow, content):
        def __init__(self):
            ComponentWindow.__init__(self,'Mixin','Main')
            content.__init__(self)

    contentmix()

    class contentsub(PopupWindow, content):
        def __init__(self):
            PopupWindow.__init__(self,'Popup','subclass')
            content.__init__(self)
    contentsub()

    #non-class usage
    win = PopupWindow()
    Button(win, text='Redwood', command=win.quit).pack()
    Button(win, text='Sing', command=win.destroy).pack()
    mainloop()
if __name__ == '__main__':
    _selftest()


