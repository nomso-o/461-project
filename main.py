#!/usr/bin/env python
'''
##############################
Create Gui window
##############################
'''
import sys
import threading 
from tkinter import *
from tkinter.messagebox import showinfo, showerror
from tkinter.simpledialog import askfloat
from tkinter.filedialog import askopenfilename
from shellgui import ListMenuGui
from windows import MainWindow
from scrolledtext import ScrolledText
from makedb import makedb
from conndb import dblogin
from makedb import makedb_Wrapper
from makedicts import makedicts
from guiStreams import redirectGuiFunc
from grid import SumGrid
from queries import runqueryDialog, searchdlg, insertdlg, deletedlg, updatedlg
from scrolledcanvas import ScrolledCanvas

default = 'select * from product'

class AppMain(ListMenuGui):
    def __init__(self, user,dbname):
        self.myMenu = [
            ('Load database', lambda : threading.Thread(target=self.loaddb).start()),
            ('Insert', lambda parent=self : insertdlg(parent)),
            ('Update Record', lambda parent=self : updatedlg(parent)),
            ('Delete', lambda parent=self : deletedlg(parent)),
            ('Search Record', lambda parent = self: searchdlg(parent) ),

        ]
        self.conn, self.cur = dblogin(user=user, dbname=dbname)
        ListMenuGui.__init__(self)
        t = threading.Thread(target=self.loadrows)
        t.start()
             
    def makeWidgets(self):
        grid = SumGrid(parent=self, numcol=7)
        grid.config(bd=6, padx=3,pady=4)
        grid.pack(expand=YES,fill=BOTH)
        self.grid_ = grid
           

    def loaddb(self):
        filename = askopenfilename()
        makedb_Wrapper(self.conn,self.cur,file=filename)
        self.result = redirectGuiFunc(self.makeQuery,self.cur, default)
        self.grid_.load_table(self.result)
    
    def makeQuery(self, *args, **kwargs):
        rows = makedicts(*args, **kwargs)
        return rows[:30]
    
    def loadrows(self):
        request = self.makeQuery(self.cur, default)
        self.grid_.load_table(request)

    def update_table(self, query='', params=()):
        if not query:
            showinfo('Query Error', 'Please enter a sound query')
        else:
            try:
                self.cur.execute(query,params)
                self.conn.commit()
            except Exception as err:
                showerror('Error',err)
        return self.cur.rowcount


if __name__ == '__main__':
    name = 'Sql Demo'
    AppMain('postgres','gui_db').mainloop()
