#!/usr/bin/env python
'''
########################################################################
wrap up widget construction in fuctions for easier use, base open some
assuptions (e.g., expansion); use **extras fkw args for width, font/color,
e.t.c., and repark result manually later to override defaults if needed;
#########################################################################
'''
from tkinter import *

def frame(root,side=TOP, **extras):
    widget = Frame(root)
    widget.pack(side=side, expand=NO, fill=X)
    if extras: widget.config(**extras)
    return widget

def label(root,side,text,**extras):
    widget = Label(root,text=text,relief=RIDGE)
    widget.pack(side=side,expand=YES,fill=BOTH)
    if extras: widget.config(**extras)
    return widget

def button(root,text,command,side=TOP,**extras):
    widget = Button(root,text=text,command=command)
    widget.pack(side=side,expand=YES,fill=BOTH)
    if extras: widget.config(**extras)
    return widget
 
def entry(root,side,linkvar,**extras):
    widget = Entry(root,relief=SUNKEN,textvariable=linkvar)
    widget.pack(side=side,expand=YES,fill=BOTH)
    if extras: widget.config(**extras)
    return widget

if __name__ == '__main__':
    app = Tk()
    frm = frame(app)
    label(frm,LEFT,'SPAM')
    button(frm,BOTTOM,'Press', lambda : print('pushed'))
    mainloop()
    