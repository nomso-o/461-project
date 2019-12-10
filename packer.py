#!/usr/bin/env python
'''
##############################################
pack file into a single file (simple archive)
##############################################
'''
import sys, os
marker =":"*20 + 'textpack=>'

def pack(ofile,ifiles):
    output = open(ofile,'w')
    for name in ifiles:
        print('[*] packing', name)
        input = open(name,'r').read()
        if input[-1] != '\n': input += '\n'
        output.write(marker + name + '\n')
        output.write(input)

if __name__ == '__main__':
    infiles = []
    if len(sys.argv) > 2:
        infiles = sys.argv[2:]
        pack(sys.argv[1], infiles)
    else:
        print('[-] please enter output file and input files')
    