#!/usr/bin/env python
'''
#######################################
create database connection 
and create database schema
#######################################
'''
import psycopg2
from tkinter.messagebox import showerror
SCHEMA = 'CREATE TABLE {} \
(InvoiceNo varchar(20) not null,\
StockCode varchar(20) not null,\
Description text ,\
Quantity integer ,\
InvoiceDate timestamp,\
UnitPrice money ,\
CustomerId varchar(20) ,\
Country varchar(20))'

def dblogin(dbname='test', user='postgres', host='localhost',port='5432', table='product', password=''):
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, host=host,port=port, password=password)
        cur = conn.cursor()
        #query = SCHEMA.format(table)
        #cur.execute(query)
        conn.commit()
        return conn, cur
    except Exception as er:
        showerror('Db Error', er)
        conn, cur = login(dbname=dbname, user=user, host=host,port=port, table=table)
        return conn, cur

def login(dbname='test', user='postgres', host='localhost',port='5432', table='product'):
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, host=host,port=port)
        cur = conn.cursor()
        return conn, cur
    except:
        pass

if __name__ == '__main__':
    dblogin(dbname='gui_db',user='postgres')





