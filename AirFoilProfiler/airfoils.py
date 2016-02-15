
#-------------------
#-------------------

## @package MINTAKA
#  @authors Celestica's Team
#  @brief Module to communicate with Betelgeuse devices.
#  @date 11/12/2014
#  @version v1.0.1
#
#  @details This module contains a Betelgeuse TCP client and server classes
#   to control the device remotely. On the other hand, this file can be run it
#   directly like as a tiny betelgeuse server.

#-------------------
#-------------------

import os
import sys
from PIL import Image, ImageTk
import numpy as np
import cv2

#------------------
#----  VERSION ----

MAJOR = '0'
MINOR = '1'
PATCH = '0'

VERSION = MAJOR + '.' + MINOR + '.' + PATCH

#------------------
#--  CONSTANTS ----

DESTINATION_FOLDER = '.\\AIRFOILS'

#------------------
#----  METHODS ----

## getFiles TCP client
#
# @details This method returs all '.dat' and '.cor' files from the
#  rootdir folder and subfolders
#  @param rootdir folder to be analized.
#  @return file's path list
def getFiles(rootdir):
    Rslt = []
    for root, subFolders, files in os.walk(rootdir):
        for a in files:
            Rslt.append(root + '\\' + a)
    return Rslt

def getCoordsFromFile(filePath):
    pass

def getFileName(filePath):
    pass

def readFile(filePath):
    with open(filePath) as f:
        lines = f.read().splitlines()

def filterList(fileList):
    Rslt = []
    for a in fileList:
        if '.dat' in a or '.cor' in a:
            Rslt.append(a)
    return Rslt

def createImage():
    return cv2.imread('.\\10ppm.bmp')


def createDestinationFolder():
    if os.path.exists(DESTINATION_FOLDER):
        for a in getFiles(DESTINATION_FOLDER):
            os.remove(a)
        os.rmdir(DESTINATION_FOLDER)
    os.makedirs(DESTINATION_FOLDER)

#------------------
#------  MAIN -----

## Main Entry
# @details If the program is run directly or passed as an argument to the python
#  interpreter then create a tiny Mintaka Server
if __name__ == "__main__":
    fileList = filterList(getFiles('.\\'))
    if len(fileList):
        createDestinationFolder()
        #for f in fileList:
    img = createImage()
    print img[100,100]
    img.itemset((100,100,0),0)
    cv2.imwrite('.\\kk.bmp',img)


#------------------
#------------------
