#!/usr/bin/env python
'''
##################################
load database from csv file
##################################
'''
from tkinter import *
from csvreader import csv_reader_Wrapper
def login(dbfile):
    import sqlite3
    conn = sqlite3.connect('dbase1')
    curs = conn.cursor()
    return conn, curs

def loaddb():
    colname, rowdata = csv_reader_Wrapper()
    conn, curs = login
    #curs.excute('create table')


if __name__ == '__main__':
    root = Tk()
    Button(root,text='load csv',command= loaddb).pack(fill=X)
    root.mainloop()