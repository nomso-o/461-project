#!/usr/bin/env python
'''
######################################################################
create a label+entry row frame, with optional file open browe button;
######################################################################
'''

from tkinter import *
from tkinter.filedialog import askopenfilename

def makeFormRow(parent,label,width=25,browse=True, extend=False):
    var = StringVar()
    row = Frame(parent)
    lbl = Label(row, text=label + "?", relief=RIDGE, width=width)
    ent = Entry(row, relief=SUNKEN, textvariable=var)
    row.pack(fill=X)
    lbl.pack(side=LEFT)
    ent.pack(side=LEFT, expand=YES, fill=X)
    if browse:
        btn = Button(row, text='browse...')
        btn.pack(side=RIGHT)
        if not extend:
            btn.config(command= lambda : var.set(askopenfilename() or var.get() ))
        else:
            btn.config(command = lambda : var.set( var.get() + ' ' + askopenfilename()))
    return var

def makeFormRowString(parent,label,width=25,browse=True, extend=False):
    var = StringVar()
    row = Frame(parent)
    lbl = Label(row, text=label + "?", relief=RIDGE, width=width)
    ent = Entry(row, relief=SUNKEN, textvariable=var)
    row.pack(fill=X)
    lbl.pack(side=LEFT)
    ent.pack(side=LEFT, expand=YES, fill=X)
    if browse:
        btn = Button(row, text='browse...')
        btn.pack(side=RIGHT)
        if not extend:
            btn.config(command= lambda : var.set(askopenfilename() or var.get() ))
        else:
            btn.config(command = lambda : var.set( var.get() + ' ' + askopenfilename()))
    return var

def makeFormRowInt(parent,label,width=25,browse=True, extend=False):
    var = IntVar()
    row = Frame(parent)
    lbl = Label(row, text=label + "?", relief=RIDGE, width=width)
    ent = Entry(row, relief=SUNKEN, textvariable=var)
    row.pack(fill=X)
    lbl.pack(side=LEFT)
    ent.pack(side=LEFT, expand=YES, fill=X)
    if browse:
        btn = Button(row, text='browse...')
        btn.pack(side=RIGHT)
        if not extend:
            btn.config(command= lambda : var.set(askopenfilename() or var.get() ))
        else:
            btn.config(command = lambda : var.set( var.get() + ' ' + askopenfilename()))
    return var

def makeFormRowDouble(parent,label,width=25,browse=True, extend=False):
    var = DoubleVar()
    row = Frame(parent)
    lbl = Label(row, text=label + "?", relief=RIDGE, width=width)
    ent = Entry(row, relief=SUNKEN, textvariable=var)
    row.pack(fill=X)
    lbl.pack(side=LEFT)
    ent.pack(side=LEFT, expand=YES, fill=X)
    if browse:
        btn = Button(row, text='browse...')
        btn.pack(side=RIGHT)
        if not extend:
            btn.config(command= lambda : var.set(askopenfilename() or var.get() ))
        else:
            btn.config(command = lambda : var.set( var.get() + ' ' + askopenfilename()))
    return var