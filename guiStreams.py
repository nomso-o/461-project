#!/usr/bin/env python
'''
################################################
Class implementation for GUI redirection streams
behave almost like built-in file object
################################################
'''
from tkinter import *
from tkinter.simpledialog import askstring
from scrolledtext import ScrolledText

class GuiOutput:
    font = ('courier', 9, 'normal')
    def __init__(self, parent=None):
        self.text = None
        if parent:
            self.popupnow(parent)
    
    def popupnow(self, parent=None):
        if self.text: return
        self.text = ScrolledText(parent or Toplevel())
        self.text.text.config(font=self.font, width=150)
    
    def write(self,text):
        self.popupnow()
        self.text.text.insert(END, str(text))
        self.text.text.update()
        self.text.text.see(END)
    
    def writelines(self, lines):
        for line in lines: self.write(line)

class GuiInput:
    def __init__(self):
        self.buff = ''
    
    def inputLine(self):
        line = askstring('GUIInput', 'Enter input line + <ctrlf> (cancel=eof)')
        if line == None:
            return ''
        else:
            return line + '\n'
    
    def read(self, bytes_=None):
        if not self.buff:
            self.buff = self.inputLine()
        if bytes_:
            text = self.buff[:bytes_]
            self.buff = self.buff[bytes_:]
        else:
            text = ''
            line = self.buff
            while line:
                text = text + line
                line = self.inputLine()
        return text 
    
    def readline(self):
        text = self.buff or self.inputLine()
        self.buff = ''
        return text

    def readlines(self):
        lines = []
        while  True:
            next = self.readline()
            if not text: break
            lines.append(next)
        return lines

def redirectGuiFunc(func, *pargs, **kwargs):
    import sys
    saveStreams = sys.stdin, sys.stdout, sys.stderr
    sys.stdin = GuiInput()
    sys.stdout = GuiOutput()
    sys.stderr = sys.stdout
    result = func(*pargs, **kwargs) # is a blocking call where the foreign function is executed
    sys.stdin, sys.stdout, sys.stderr = saveStreams
    return result

def redirectedGuiShellCmd(command):
    import os
    input_ = os.popen(command,'r')
    output = GuiOutput()

    def reader(input_, output):
        while True:
            line = input_.readline()
            if not line: break
            output.write(line)
    reader(input_, output)

if __name__ == '__main__':
    def makeUpper():
        while True:
            try:
                line = input('Line?')
            except:
                break
            print(line.upper())
        print('end of file')
    
    def makeLower(input, output):
        while True:
            try:
                line = input.readline()
            except:
                break
            output.write(line.lower())
        print('end of file')
    
    root = Tk()
    Button(root, text='test streams', command= lambda :redirectGuiFunc(makeUpper)).pack(fill=X)
    Button(root, text='test files', command= lambda : makeLower(GuiInput(),GuiOutput())).pack(fill=X)
    Button(root, text='test popen', command= lambda : redirectedGuiShellCmd('ls ../')).pack(fill=X)
    root.mainloop()




