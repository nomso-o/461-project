#!/usr/bin/env python
'''
GUi demo implementation - combines makes, mixin, and this
'''
import os, sys
from tkinter import *
from guimixin import GuiMixin
from guimaker import GuiMakerWindowMenu
import widgets

class Hello(GuiMixin, GuiMakerWindowMenu):
    def start(self):
        self.hellos = 0
        self.master.title('GuiMaker Demo')

        self.menuBar = [
            ('File',0,[('Open', 0, self.browser),('Quit', 0, self.quit)]),
        ]
        self.toolBar = [
            ('Quit', self.quit, {'side':RIGHT}),
            ('Hello', self.greeting, {'side':LEFT}),
            ('Pop-up', self.dialog, {'side':LEFT}),

        ]
    def makeWidgets(self):
        widgets.label(self,TOP,text='Hellow maker world!',width=40,height=10,relief=SUNKEN, cursor='pencil',bg='white')
    
    def greeting(self):
        self.hellos += 1
        if self.hellos % 3:
            print('hi')
        else:
            self.infobox('Three','HELLO!')
    def dialog(self):
        button =self.question('OOPS!' ,'You typed "rm*" ...continue?','questhead', ('yes', 'no'))
        [lambda:None, self.quit][button]()

if __name__ == '__main__':
    Hello().mainloop()