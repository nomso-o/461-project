#!/usr/bin/env python
'''
####################################
Read data from a csv file 
####################################
'''
import csv, time
from tkinter import *
from guiStreams import redirectGuiFunc

def read_csv(file=None):
    line_count = 0
    data = ''
    output = []
    names = ''
    if not file:
        print('[-] No input file')
        return
    with open(file) as csv_file:
        try:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if line_count == 0:
                    names = row
                    output.append(row)
                    data += '{}\n'.format('\t\t'.join(row))
                    line_count += 1
                    #time.sleep(0.5)
                else:
                    output.append(row)
                    data += '{}\n'.format('\t\t'.join(row))
                    line_count +=1
            print('{} \n {}:lines'.format(data, line_count))
        except:
            print('{} \n {}:lines'.format(data, line_count))
    return names, output

def csv_reader_Wrapper(file='Online Retail.csv'):
    result = redirectGuiFunc(read_csv,file )
    return result

if __name__ == '__main__':
    app = Tk()
    Button(app, text='test', command=csv_reader_Wrapper).pack(fill=X)

    app.mainloop()