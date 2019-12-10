#!/usr/bin/env python
''' 
####################################################
pop Gui dialog for unpacker arguments, and run it
####################################################
'''

from tkinter import *
from unpacker import unpack
from formrows import makeFormRow
from guiStreams import redirectGuiFunc

def unpackDialog():
    win = Toplevel()
    win.title('Enter Unpack Parameters')
    var = makeFormRow(win, label='Input file', width=11)
    #Button(win,text='OK', command=win.destroy())
    win.bind('<Key-Return>', lambda event: win.destroy())
    win.grab_set()
    win.focus_set()
    win.wait_window()
    return var.get()

def runUnpackDialog():
    input = unpackDialog()
    if input != '':
        print('[*] Unpacker ', input)
        unpack(infile=input)

##############################################
# unpacked dialog wrapped
##############################################
def runUnpackDialog_Wrapped():
    redirectGuiFunc(runUnpackDialog)

if __name__ == '__main__':
    Button(None, text='Pop-up', command=runUnpackDialog).pack()
    mainloop()
    