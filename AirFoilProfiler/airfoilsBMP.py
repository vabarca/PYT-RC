
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
import unittest
from airfoilsUtils import *

#------------------
#----  VERSION ----

MAJOR = '0'
MINOR = '1'
PATCH = '0'

VERSION = MAJOR + '.' + MINOR + '.' + PATCH

#------------------
#--  CONSTANTS ----

_DEBUG = 0

_X = 400
_Y = 1000

DESTINATION_FOLDER = './AIRFOILS'

#------------------
#----  METHODS ----

def getCoordsFromFile(filePath):
    dots = []
    with open(filePath) as f:
        for line in f.read().splitlines():
            coords = line.split()
            if len(coords)==2:
                if (isfloat(coords[0]) and isfloat(coords[1])):
                    y = int(float(coords[0])*999)
                    x = int(float(coords[1])*999)+(_X/2)
                    dots.append((x,y))
    return dots

def getDestFilePath(filePath):
    path, filename = os.path.split(filePath)
    filename = filename.replace('.dat','.bmp')
    filename = filename.replace('.cor','.bmp')
    return DESTINATION_FOLDER + '/' + filename

def getBaseImage():
    return cv2.imread('./10ppmm.bmp',cv2.IMREAD_GRAYSCALE)

def addAuxiliarLines(img):
  cv2.line(img,(_X/2,0),(_X/2,_Y-1),(128,128,128),1)
  slices = 40
  fract = 1000/slices
  for i in range(slices):
    cv2.line(img,(0,fract * i),(_X-1,fract * i),(128,128,128),1)

def createDestinationFolder():
    if os.path.exists(DESTINATION_FOLDER):
        for a in getFiles(DESTINATION_FOLDER):
            os.remove(a)
        os.rmdir(DESTINATION_FOLDER)
    os.makedirs(DESTINATION_FOLDER)

def convertDATA2BMP(strFilePath):
    img = getBaseImage()
    addAuxiliarLines(img)
    dots = getCoordsFromFile(strFilePath)
    for i in range(len(dots)-1):
        cv2.line(img,dots[i], dots[i+1],(0,0,0),2)
    docBMP = getDestFilePath(strFilePath)
    cv2.imwrite(docBMP,img)
    print docBMP
    return docBMP

def convertDATA2BMPs(strFolder):
    fileList = filterList(getFiles(strFolder),'.dat') \
     + filterList(getFiles(strFolder),'.cor')
    count = 0
    if len(fileList):
        createDestinationFolder()
        for f in fileList:
            convertDATA2BMP(f)
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
        convertDATA2BMP('./')

#------------------
#------  MAIN -----

## Main Entry
# @details If the program is run directly or passed as an argument to the python
#  interpreter then create a tiny Mintaka Server
if __name__ == "__main__":
    unittest.main()

#------------------
#------------------
