#!/usr/bin/env python
'''
####################################################
provide type-specific option for application
####################################################
'''
from shellgui import *
from unpackdlg import runUnpackDialog
from packdlg import runPackDialog_Wrapped
from unpackdlg import runUnpackDialog_Wrapped

class Textpak1(ListMenuGui):
    def __init__(self):
        self.myMenu = [
            ('Pack', lambda : runPackDialog_Wrapped()),
            ('Unpack', lambda : runUnpackDialog_Wrapped()),
            ('Mtool', lambda title='Yea', text='You have reached your commands': ListMenuGui.question(self,title,text)),

        ]
        ListMenuGui.__init__(self)
    
    def forToolBar(self,label):
        return label in {'Pack','Unpack'}

class Textpak2(DictMenuGui):
    def __init__(self):
        self.myMenu = {
            'Pack': lambda title='Yea', text='You have reached your commands': question(self,title,text),
            'Unpack': lambda title='Yea', text='You have reached your commands': question(self,title,text),
            'Mtool':  lambda title='Yea', text='You have reached your commands': question(self,title,text),

        }
        DictMenuGui.__init__(self)

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'list':
        print('list test')
        Textpak1().mainloop()
    else:
        print('dict test')
        Textpak2().mainloop()
