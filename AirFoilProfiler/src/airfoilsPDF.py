
#-------------------
#-------------------

## @package AirFoilsPDF
#  @authors TT
#  @brief Print airfoil profiles from BMP (400x1000) to scaled PDF file
#  @date 18/02/2016
#  @version v0.1.1
#
#  @details This file constains the methods required for creating PDF airfoil files
#  from BMP files in the working directory

#-------------------
#-------------------

import os
import sys
import unittest
import numpy as np
import cv2
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm, mm
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from airfoilsUtils import *

#------------------
#----  VERSION ----

MAJOR = str(0)
MINOR = str(1)
PATCH = str(1)

VERSION = MAJOR + '.' + MINOR + '.' + PATCH

#------------------
#--  CONSTANTS ----

_DEBUG = 0

#------------------
#----  METHODS ----

def convertBMP2PDF(strFilePath, realSize, strFolderDest = None):
    if not os.path.isfile(strFilePath):
        return
    img = cv2.imread(strFilePath,cv2.IMREAD_GRAYSCALE)
    imgSize = tuple(img.shape[1::-1])
    docPDF = strFilePath.replace('.bmp','.pdf')
    if strFolderDest:
        createFolder(strFolderDest,False)
        p, f = os.path.split(os.path.realpath(docPDF))
        docPDF = os.path.normpath(strFolderDest + '/' + f)
    c = canvas.Canvas(docPDF, pagesize=A4)
    xSize = (realSize*imgSize[0]*mm)/imgSize[1]
    ySize = realSize*mm
    xPos = (210*mm/2 - xSize/2)
    yPos = (290*mm/2 - ySize/2)
    c.drawImage(strFilePath, xPos , yPos , xSize , ySize)
    c.showPage()
    c.save()
    print docPDF
    if _DEBUG == 1:
        print xSize
        print ySize
        print xPos
        print yPos
    return docPDF

def convertBMP2PDFs(strFolderOri, realSize, strFolderDest = None):
    fileList = filterList(getFiles(strFolderOri),'.bmp')
    count = 0
    if len(fileList):
        for f in fileList:
            convertBMP2PDF(f,realSize, strFolderDest)
            count = count + 1
            if _DEBUG == 1:
                return
    print ('Processed ' + str(count) + ' of ' + str(len(fileList)) + ' files')

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
        p, f = os.path.split(os.path.realpath(__file__))
        p = os.path.normpath(p)
        convertBMP2PDFs(p,150,os.path.normpath(p + '/PDFs'))

#------------------
#------  MAIN -----

## Main Entry
# @details If the program is run directly or passed as an argument to the python
#  interpreter then create a tiny Mintaka Server
if __name__ == "__main__":
    unittest.main()

#------------------
#------------------
