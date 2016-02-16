
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

#------------------
#----  VERSION ----

MAJOR = '0'
MINOR = '1'
PATCH = '0'

VERSION = MAJOR + '.' + MINOR + '.' + PATCH

#------------------
#--  CONSTANTS ----

DESTINATION_FOLDER = './AIRFOILS'

#------------------
#----  METHODS ----

def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False

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
            Rslt.append(root + '/' + a)
    return Rslt

def getCoordsFromFile(filePath):
    dots = []
    with open(filePath) as f:
        for line in f.read().splitlines():
            coords = line.split()
            if len(coords)==2:
                if (isfloat(coords[0]) and isfloat(coords[1])):
                    x = int(float(coords[0])*999)
                    y = int(float(coords[1])*999)+200
                    dots.append((x,y))
    return dots

def getDestFilePath(filePath):
    path, filename = os.path.split(filePath)
    filename = filename.replace('.dat','.bmp')
    filename = filename.replace('.cor','.bmp')
    return DESTINATION_FOLDER + '/' + filename

def filterList(fileList):
    Rslt = []
    for a in fileList:
        if '.dat' in a or '.cor' in a:
            Rslt.append(a)
    return Rslt

def getBaseImage():
    return cv2.imread('./10ppmm.bmp',cv2.IMREAD_GRAYSCALE)

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
    fileList = filterList(getFiles('./'))
    if len(fileList):
        createDestinationFolder()
        for f in fileList:
            img = getBaseImage()
            #height, width, channels = img.shape
            dots = getCoordsFromFile(f)
            for i in range(len(dots)-1):
                cv2.line(img,dots[i], dots[i+1],(0,0,0),2)
            dest = getDestFilePath(f)
            cv2.imwrite(dest,img)
            print dest

#------------------
#------------------

