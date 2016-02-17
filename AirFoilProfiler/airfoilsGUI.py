
#-------------------
#-------------------

## @package AirFoils
#  @authors TT
#  @brief Parse airfoil files and create profiles images en a 1000x400 bmp file.
#  @date 16/02/2016
#  @version v0.1.0
#
#  @details This file constains the methods required for parsing airfoil files
#  from working directory and for creating 1000x400 bmp files with the
#  corresponding profile data

#-------------------
#-------------------

import os
import sys
import numpy as np
import cv2
from Tkinter import *
import tkMessageBox
import unittest
from airfoilsUtils import *
from airfoilsPDF import *
from airfoilsBMP import *

#------------------
#----  VERSION ----

MAJOR = '0'
MINOR = '1'
PATCH = '0'

VERSION = MAJOR + '.' + MINOR + '.' + PATCH

#------------------
#--  CONSTANTS ----

_DEBUG = False

#------------------
#----  GLOBALS ----

gBMPFiles = []

#------------------
#----  METHODS ----

def mainGUI(strFolder):
    global gBMPFiles
    gBMPFiles = filterList(getFiles(strFolder),'.bmp')

    top = Tk()

    #------

    scrollbar = Scrollbar(top)
    scrollbar.pack( side = RIGHT, fill=Y )

    fileListBox = Listbox(top, yscrollcommand = scrollbar.set )

    for f in gBMPFiles:
        head, tail = os.path.split(f)
        fileListBox.insert(END, tail)

    fileListBox.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = fileListBox.yview )

    fileListBox.bind('<<ListboxSelect>>', onselectListBoxCallBack)

    #------

    var = StringVar()
    labelCtrl = Label( top, textvariable=var)
    var.set('Chord lenght (mm):')
    labelCtrl.pack()

    spinBoxCtrl = Spinbox(top, from_=20, to=290, validate='all')
    spinBoxCtrl.pack()

    #------

    buttonCtrl = Button(top, text ="Generate PDF", command = createPDFCallBack)
    buttonCtrl.pack()

    #------

    top.mainloop()

#-------------------
#----  CALLBACK ----

def createPDFCallBack():
    tkMessageBox.showinfo( "Hello Python", "Hello World")

def onChangeSpinBoxCallBack(s, S):
    tkMessageBox.showinfo( "Hello Python", "Hello World")

def onselectListBoxCallBack(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    img = cv2.imread(gBMPFiles[index],cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Profile', cv2.resize(img, (200, 500)) )
    if _DEBUG:
        print 'You selected item %d: "%s"' % (index, value)

#-----------------------
#------  UNITTES -------

## Unittest purposes
class CUnit_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print ('Running CUnit_test ...')

    @classmethod
    def tearDownClass(cls):
        print ('CUnit_test finish!')

    #------------

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #------------
    #@unittest.skip("demonstrating skipping")
    #@unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    @unittest.skipIf(True,"Skip it!")
    def test_skip_it(self):
        pass

    def test_execute(self):
        mainGUI('./')

#------------------
#------  MAIN -----

## Main Entry
# @details If the program is run directly or passed as an argument to the python
#  interpreter then create a tiny Mintaka Server
if __name__ == "__main__":
    unittest.main()

#------------------
#------------------
