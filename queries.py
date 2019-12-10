#!/usr/bin/env python
'''
###############################################
sql queries to automate search
###############################################
'''

from tkinter import *
from tkinter.messagebox import *
from tkinter.simpledialog import askfloat
from widgets import label, frame, button
from formrows import makeFormRow, makeFormRowInt
from makedicts import makedicts
from guiStreams import redirectGuiFunc
Queries = {
'RANGE' : 'SELECT * FROM {} WHERE {} BETWEEN {} AND {}',
'SPECIFIC-SEARCH' : 'SELECT * FROM {} WHERE {}',
'UPDATE' : 'UPDATE {} SET {} WHERE {}',
'DELETE' : 'DELETE FROM {} WHERE {}',
'INSERT' : 'INSERT INTO {} VALUES ({})',
'SEARCH' : 'SELECT * FROM {} WHERE {}'
}
##################################################
#update dialog used by the client to parse queries
##################################################

#################################################
# Globals
#################################################
DATA = ''
TABLE = 'product'
#################################################

def queryDialog():
    win = Toplevel()
    win.title('Enter Record')
    var1 = makeFormRow(win,label='column',browse=False)
    var2 = makeFormRow(win, label='condition', browse=False)
    Button(win, text='OK', command=win.destroy).pack()
    win.grab_set()
    win.focus_set()
    win.wait_window()
    return var1.get(), var2.get()

def runqueryDialog():
    output, output1 = queryDialog()
    if output != '' and output1 != '':
        print('add logic')
############################################################
def search(parent,user=None):
    temp = {}
    def validate():
        for var in [var1, var2, var3]:
            if var == var1:
                val = var.get()
                try:
                    if val != 0:
                        temp['InvoiceNo'] = val
                except Exception as err:
                    showerror('Type Error', err)
                    print(err)
            if var == var2:
                val = var.get()
                try:
                    if val != 0:
                        temp['CustomerID'] = val
                except Exception as err:
                    #print('Not tap')
                    showerror('Type Error', err)
                    
            if var == var3:
                val = var.get()
                try:
                    if val.isspace():
                        temp['Country'] = val
                except Exception as err:
                    showerror('Type Error', err)
        if len(temp):
            global DATA
            if user:
                DATA = user
            else:
                DATA = 'SEARCH' 
            clean(temp, parent=parent)
        win.destroy()
    win = Toplevel()
    f1 = Frame(win)
    var1 = makeFormRowInt(f1, label='InvoiceNo', browse=False)
    var2 = makeFormRowInt(f1, label='CustomerID', browse=False)
    var3 = makeFormRow(f1, label='Country', browse=False)
    f2 = Frame(win)
    Button(f2, text='Ok', command=validate).pack(expand=YES, fill=X)
    Button(f2, text='Cancel', command=win.destroy).pack(expand=YES, fill=X)
    f1.grid(row=0,column=1)
    f2.grid(row=0,column=2)
    win.geometry("+%d+%d" % (parent.winfo_rootx()+50,parent.winfo_rootx()+50))
    win.grab_set()
    win.focus_set()
    win.wait_window()
                


def searchdlg(*args):
    if askyesno("Search",'Do you wish to search for a record?'):
        redirectGuiFunc(search, *args)
##########################################################################
def insert_record(parent):
    win = Toplevel()
    f1 = Frame(win)
    column = [col[0] for col in parent.cur.description]
    temp = []
    for name in column:
        temp.append(makeFormRow(f1, label=name, browse=False))
    f2 = Frame(win)
    Button(f2, text='Ok', command=ss).pack(expand=YES, fill=X)
    Button(f2, text='Cancel',command=win.destroy).pack(expand=YES, fill=X)
    f1.grid(row=0,column=1)
    f2.grid(row=0,column=2)
    win.geometry("+%d+%d" % (parent.winfo_rootx()+50,parent.winfo_rootx()+50))
    win.grab_set()
    win.focus_set()
    win.wait_window()
    new_record = dict(zip(column,temp))
    global DATA 
    DATA = 'INSERT'
    def ss():
        if new_record:
            clean(new_record,parent)
        win.destroy()

def insertdlg(*args):
    if askyesno("Insert",'Do you wish to insert  a  given record?'):
        insert_record(*args)
##################################################################################
def update_table(parent,query='', params=()):
    if not query:
        showinfo('Query Error', 'Please enter a sound query')
    else:
        try:
            parent.cur.execute(query,params)
            parent.conn.commit()
            showinfo('Sucess', 'Sucessful update and commit')
        except Exception as err:
            parent.conn.rollback()
            showerror('Error',err)
        return parent.cur.rowcount
####################################################################################
def clean(data,parent=None):
    global DATA
    names = [name for name in data.keys()]
    values = [val for val in data.values()]
    row = dict(zip(names,values))
    #print(Queries,'\n',DATA)
    if DATA not in Queries.keys():
        showinfo('Query Error','Unknown command')
    elif DATA == 'INSERT':
        placeholder = []
        for v in values:
            placeholder.append('%s')
        query = Queries[DATA]
        vals = [val.get() for val in values]
        query = query.format(TABLE,','.join(placeholder))
        #print(query)
        update_table(parent,query, params=vals)
    elif DATA == 'SEARCH':
        command = []
        for i in range(len(values)):
            command.append(f'{names[i]} = \'{values[i]}\'')
        #print(command)
        if len(command):
            a = command[0]
            b = command[1]
            condition = f'{a} AND {b}'
            query = Queries[DATA]
            #print(query)
            query = query.format(TABLE,condition)
            #print(query)
            result = makedicts(parent.cur,query)
            #print(result)
            pack = ''
            for data in result:
                pack += "\t\t".join([str(var) for var in data.values()])
            print(pack)
    elif DATA == 'DELETE':
        command = []
        for i in range(len(values)):
            command.append(f'{names[i]} = \'{values[i]}\'')
        #print(command)
        if len(command):
            a = command[0]
            b = command[1]
            condition = f'{a} AND {b}'
            query = Queries[DATA]
            #print(query)
            query = query.format(TABLE,condition)
            #print(query)
            update_table(parent, query)
    elif DATA == 'UPDATE':
        pass
###########################################################################################
def deletedlg(parent):
    if askyesno('Delete Operation','Do you wish to delete a record from the database'):
        search(parent, user='DELETE')
###########################################################################################
def updatedlg(parent):
    if askyesno('Update Operation ', 'Do you wish to update a record'):
        search(parent, user='UPDATE')

if __name__ == '__main__':
    runqueryDialog()
    

