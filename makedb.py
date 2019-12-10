#!/usr/bin/env python
'''
###############################################
create create or delete a database 
###############################################
'''

import sys, time
from tkinter import *
from tkinter.messagebox import showinfo, askyesno, showerror
from loaddb import login
from csvreader import read_csv
from guiStreams import redirectGuiFunc
from conndb import dblogin

def makedb(con,curs,table='product',file=None):
    if not askyesno('Db','Do you wish to create database with name: ' + file):
        return

    try:
        names, rows = read_csv(file)
        placeholder = []
        for name in names:
            placeholder.append('%s')
        for row in rows[1:]:
            query = 'insert into {} values ({})'.format(table,",".join(placeholder))
            curs.execute(query,row)
        con.commit()
        showinfo('Sucess', 'You have loaded the file into data base')
    except Exception as er:
        print(er)
        showerror('Error', er)   
                
    

def makedb_Wrapper(*args,**kwargs):
    redirectGuiFunc(makedb,*args,**kwargs)

if __name__ == '__main__':
    root = Tk()
    conn, curs = dblogin(dbname='gui_db',user='postgres')
    Button(root, text='make database', command= lambda conn=conn, curs=curs: makedb_Wrapper(conn,curs)).pack(fill=X)
    root.mainloop()
    
