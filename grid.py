#!/usr/bin/env python
'''
cell table created as a reusable class
'''

from tkinter import *
from tkinter.filedialog import askopenfilename
from quitter import Quitter
trace = True
class SumGrid(Frame): 
    def __init__(self, parent=None, numrow=5,numcol=5,flag=None):
        Frame.__init__(self,parent)
        self.numrow = numrow
        self.numcol = numcol
        self.flag = flag
        self.makeWidgets(numrow, numcol)
        

    def makeWidgets(self,numrow, numcol):
        self.rows = []
        #total sums
        self.sums = []
        if self.flag:    
            for num, val in enumerate(self.flag):
                b = Button(self,text=val[0].upper())
                b.config(bd=3)
                b.grid(row=0, column=num,  sticky=NSEW)

        for i in range(numrow):
            cols = []
            for j in range(numcol):
                ent = Entry(self,relief=RIDGE)
                ent.grid(row=i+1, column=j, sticky=NSEW)
                ent.insert(END,'%d.%d' % (i,j))
                cols.append(ent)
            self.rows.append(cols)
        '''
        Button(self,text='Sum', command=self.onSum).grid(row=0, column=0)
        Button(self,text='fetch', command=self.onPrint).grid(row=0, column=1)
        Button(self,text='clear', command=self.onClear).grid(row=0, column=2)
        Button(self,text='load', command=self.onLoad).grid(row=0, column=3)
        '''

    def onPrint(self):
        for row in self.rows:
            for col in row:
                print(col.get(), end=' ')
            print()
        print()

    def onSum(self):
        tots = [0] * self.numcol
        for i in range(self.numcol):
            for j in range(self.numrow):
                tots[i] += eval(self.rows[j][i].get())
        for i in range(self.numcol):
            if trace:
                print(i)
            self.sums[i].config(text=str(tots[i]))

    def onClear(self):
        for row in self.rows:
            for col in row:
                col.delete('0',END)
                col.insert(END, '0.0')
        for sum in self.sums:
            sum.config(text='?')

    def onLoad(self):
        file = askopenfilename()
        if file:
            for row in self.rows:
                for col in row:
                    col.forget()
            for sum in self.sums:
                sum.grid_forget()
        filelines = open(file, 'r').readlines()
        self.numrow = len(filelines)
        self.numcol = len(filelines[0].split())
        if trace:
            print('numrow: ', self.numrow)
            print('numcol: ', self.numcol)
        self.makeWidgets(self.numrow, self.numcol)

        for row, line in enumerate(filelines):
            fields = line.split()
            for col in range(self.numcol):
                self.rows[row][col].delete('0',END)
                self.rows[row][col].insert(END, fields[col])

    def load_table(self, data):
        self.numrow = len(data)
        self.numcol = len(data[0].keys())
        self.flag = data[0].items()
        self.makeWidgets(self.numrow,self.numcol)
        for num, row_ in enumerate(data):
            for num1, item in enumerate(row_.values()):
                self.rows[num][num1].delete('0', END)
                self.rows[num][num1].insert(END, item)
                self.rows[num][num1].update()


if __name__ == '__main__':
    import sys
    root = Tk()
    root.title('summer grid')
    if len(sys.argv) != 3:
        SumGrid(root).pack()
    else:
        rows, cols = eval(sys.argv[1]), eval(sys.argv[2])
        SumGrid(root, rows, cols).pack()
    mainloop()

