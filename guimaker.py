#!/usr/bin/env python
'''
##########################################################################
An extended Frame that makes window menus and toolbars automatically.
see self test code for an example of layout tree format
##########################################################################
'''

import sys
from tkinter import *
from tkinter.messagebox import showinfo
import widgets

class GuiMaker(Frame):
    menuBar = []
    toolBar = []
    helpButton = True

    def __init__(self, parent=None):
        Frame.__init__(self,parent)
        self.pack(expand=YES, fill=BOTH)
        self.start()
        self.makeMenuBar()
        self.makeToolBar()
        self.makeWidgets()

    def makeMenuBar(self):
        '''
        make menu bar at the top
        expand=no fill=x so same width on resize
        '''
        menubar = widgets.frame(self, relief=SUNKEN, bd=2)

        for (name, key, items) in self.menuBar:
            mbutton = Menubutton(menubar,text=name, underline=key)
            mbutton.pack(side=LEFT)
            pulldown = Menu(mbutton)
            self.addMenuItems(pulldown,items)
            mbutton.config(menu=pulldown)
    
        if self.helpButton:
            widgets.button(menubar,text='Help',cursor='gumby',relief=FLAT,command=self.help, side=RIGHT)
    def addMenuItems(self, menu, items):
        for item in items:
            if item == 'separator':
                menu.add_separator({})
            elif type(item) == list:
                for num in item:
                    menu.entryconfig(num,state=DISABLED)
            elif type(item[2]) != list:
                menu.add_command(label=item[0], underline=item[1], command=item[2])
            else:
                pullover = Menu(menu)
                self.addMenuItems(pullover, item[2])
                menu.add_cascade(label=item[0], underline=item[1], menu=pullover)
    
    def makeToolBar(self):
        '''
        make button bar at bottom, if any
        expand=no, fill=x so same width on resize
        this could support images too
        '''
        if self.toolBar:
            toolbar = widgets.frame(self,cursor='hand2',relief=SUNKEN, bd=2, side=BOTTOM)
            for (name, action, where) in self.toolBar:
               b = Button(toolbar, text=name, command=action)
               b.config(bd=2)
               b.pack(side=where['side'],expand=NO,fill=X)
    def makeWidgets(self):
        '''
        make 'middle' part last, so menu/toolbar
        is always on top/bottom and clipped last;
        for grid: grid middle part in a packed frame
        '''

        widgets.label(self,TOP,self.__class__.__name__,width=40,height=10,relief=SUNKEN,bg='white',cursor='crosshair')
    
    def help(self):
        '''override me in subclass'''
        showinfo('Help','Sorry, no help for' + self.__class__.__name__)
    
    def start(self):
        '''override in sub class to set menu/toolbar with self'''
        pass

###############################################################
# customize for main window bar , instead of a frame
###############################################################

GuiMakerFrameMenu = GuiMaker  # for embedded component menus

class GuiMakerWindowMenu(GuiMaker): # for top level windows
    def makeMenuBar(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        for (name, key, items) in self.menuBar:
            pulldown = Menu(menubar)
            self.addMenuItems(pulldown, items)
            menubar.add_cascade(label=name, underline=key, menu=pulldown)
        
        if self.helpButton:
            if sys.platform[:3] == 'win':
                menubar.add_command(label='Help',command=self.help)
            else:
                pulldown = Menu(menubar) # linux need real pull down
                pulldown.add_command(label='Help',command=self.help)
                menubar.add_cascade(label='Help', menu=pulldown)
        
if __name__ == '__main__':
    from guimixin import GuiMixin
    menuBar = [
    ('File',0,[('Open', 0, lambda:0),('Quit', 0, sys.exit)]),
    ('Edit',0,[('Paste', 0, lambda:0),('Quit', 0, lambda:0)]),
    ]

    toolBar = [('Quit', sys.exit, {'side':LEFT})]

    class TestAppFrameMenu(GuiMixin,GuiMaker):
        def start(self):
            self.menuBar = menuBar
            self.toolBar = toolBar

    root =Tk()
    TestAppFrameMenu(root)
    root.mainloop()