
#-------------------
#-------------------

## @package AirFoils
#  @authors TT
#  @brief Parse airfoil files and create profiles images en a 1000x400 JPG file.
#  @date 18/02/2016
#  @version v0.1.1
#
#  @details This file constains the methods required for parsing airfoil files
#  from working directory and for creating 1000x400 JPG files with the
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

MAJOR = str(0)
MINOR = str(1)
PATCH = str(1)

VERSION = MAJOR + '.' + MINOR + '.' + PATCH

#------------------
#--  CONSTANTS ----

_DEBUG = 0

_X = 400
_Y = 1000

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

def getDestFileName(filePath):
    path, filename = os.path.split(filePath)
    filename = filename.replace('.dat','.jpg')
    return filename.replace('.cor','.jpg')

def getBaseImage():
    p, f = os.path.split(os.path.realpath(__file__))
    p = fixPathForWindows(p)
    return cv2.imread(fixPathForWindows(p + '/10ppmm.jpg'),cv2.IMREAD_GRAYSCALE)

def addAuxiliarLines(img):
  cv2.line(img,(_X/2,0),(_X/2,_Y-1),(128,128,128),1)
  slices = 40
  fract = 1000/slices
  for i in range(slices):
    cv2.line(img,(0,fract * i),(_X-1,fract * i),(128,128,128),1)

def convertDATA2IMAGE(strFilePath, strFolderDest = None):
    if not os.path.isfile(strFilePath):
        return
    img = getBaseImage()
    addAuxiliarLines(img)
    dots = getCoordsFromFile(strFilePath)
    for i in range(len(dots)-1):
        cv2.line(img,dots[i], dots[i+1],(0,0,0),2)
    docIMAGE = getDestFileName(strFilePath)
    if strFolderDest:
        createFolder(strFolderDest,False)
        p, f = os.path.split(os.path.realpath(docIMAGE))
        docIMAGE = fixPathForWindows(strFolderDest + '/' + f)
    cv2.imwrite(docIMAGE,img)
    print (docIMAGE)
    return docIMAGE

def convertDATA2IMAGEs(strFolderOri ,strFolderDest = None):
    fileList = filterList(getFiles(strFolderOri),'.dat') \
     + filterList(getFiles(strFolderOri),'.cor')
    count = 0
    if len(fileList):
        for f in fileList:
            convertDATA2IMAGE(f, strFolderDest)
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
        convertDATA2IMAGEs(p,fixPathForWindows(p + '/AIRFOILS'))

#------------------
#------  MAIN -----

## Main Entry
# @details If the program is run directly or passed as an argument to the python
#  interpreter then create a tiny Mintaka Server
if __name__ == "__main__":
    unittest.main()

#------------------
#------------------
