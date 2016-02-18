
#-------------------
#-------------------

## @package AirFoils
#  @authors TT
#  @brief Parse airfoil files and create profiles images en a 1000x400 bmp file.
#  @date 18/02/2016
#  @version v0.1.1
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

MAJOR = str(0)
MINOR = str(1)
PATCH = str(1)

VERSION = MAJOR + '.' + MINOR + '.' + PATCH

#------------------
#--  CONSTANTS ----

_DEBUG = False

#------------------
#----  GLOBALS ----

gBMPFiles = []
gSize = 20
gIndex = 0
gListBox = None
gStrFolder = './'

#------------------
#----  METHODS ----

def updateFileBox(strFolder):
    global gBMPFiles
    global gListBox
    global gStrFolder
    gStrFolder = strFolder
    gBMPFiles = filterList(getFiles(strFolder),'.bmp')

    gListBox.delete(0, END)
    for f in gBMPFiles:
        head, tail = os.path.split(f)
        gListBox.insert(END, tail)

def mainGUI(strFolder):
    global gSize
    global gListBox

    top = Tk()

    #------

    scrollbar = Scrollbar(top)
    scrollbar.pack( side = RIGHT, fill=Y )

    gListBox = Listbox(top, yscrollcommand = scrollbar.set )
    updateFileBox(gStrFolder)

    gListBox.pack( side = LEFT, fill = BOTH )
    scrollbar.config( command = gListBox.yview )
    gListBox.bind('<<ListboxSelect>>', onselectListBoxCallBack)

    #------

    var = StringVar()
    labelCtrl = Label( top, textvariable=var)
    var.set('Chord lenght (mm):')
    labelCtrl.pack()

    spinBoxCtrl = Spinbox(top, from_=20, to=290, textvariable = gSize)
    spinBoxCtrl.pack()

    #------

    buttonCtrlPDF = Button(top, text ="Generate PDF", command = createPDFCallBack)
    buttonCtrlPDF.pack()

    buttonCtrlBMP = Button(top, text ="Generate BMP", command = createBMPCallBack)
    buttonCtrlBMP.pack()

    #------

    top.mainloop()

#-------------------
#----  CALLBACK ----

def createPDFCallBack():
    global gSize
    if type(gSize) <> int:
        gSize = 20
    if gSize > 290:
        gSize = 290
    if gSize < 20:
        gsize = 20
    convertBMP2PDF(gBMPFiles[gIndex],gSize,'./PDFs')
    tkMessageBox.showinfo( "PDF file", "PDF generated!")

def createBMPCallBack():
    global gListBox
    gListBox.delete(0,END)
    createFolder('./AIRFOILS',True)
    convertDATA2BMPs(gStrFolder,'./AIRFOILS')
    updateFileBox(gStrFolder)
    tkMessageBox.showinfo( "BMP file", "BMPs generated!")


def onselectListBoxCallBack(evt):
    global gIndex
    w = evt.widget
    gIndex = int(w.curselection()[0])
    value = w.get(gIndex)
    img = cv2.imread(gBMPFiles[gIndex],cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Profile', cv2.resize(img, (200, 500)) )
    if _DEBUG:
        print 'You selected item %d: "%s"' % (gIndex, value)

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
        mainGUI(gStrFolder)

#------------------
#------  MAIN -----

## Main Entry
# @details If the program is run directly or passed as an argument to the python
#  interpreter then create a tiny Mintaka Server
if __name__ == "__main__":
    unittest.main()

#------------------
#------------------
