
#-------------------
#-------------------

## @package restorerBackup
#  @authors Celestica's Team
#  @brief Module used to restore .py files from backup folder
#  @date 26/11/2014
#  @version v1.0
#
#  @details This module is an applications that allows restore all .py files 
#   from backup folder

#-------------------
#-------------------

import os
import sys
import glob
import time
import shutil
import getopt

#-------------------
#-------------------

path, thisFilename = os.path.split(os.path.realpath(__file__))
thisFilenameFields = thisFilename.split('.')

def printHelp():
    print('Usage: ' + thisFilename + ' -p path(without final backslash) -h help')

try:
    myopts, args = getopt.getopt(sys.argv[1:], 'p')
except getopt.GetoptError as e:
    myLogger.write(str(e))
    printHelp()
    sys.exit(1)

PATH = '../src'
PATH_BACKUP = PATH + '/BACKUP'

# o == option
# a == argument passed to the o
for o, a in myopts:
    if o == '-h':
        #Print help
        printHelp()
        sys.exit(0)
    elif o == '-p':
        try:
            PATH = str(a)
        except:
            print 'Path error'
            sys.exit(2)

fileList = glob.glob(PATH + '/*.py')
for fileName in fileList:
    p,f = os.path.split(fileName)
    if f <> thisFilename and f <> 'versioner.py':
        os.remove(fileName)

fileList = glob.glob(PATH_BACKUP + '/*.py')
for fileName in fileList:
    p,f = os.path.split(fileName)
    shutil.copy2(fileName, PATH + '/' + f)

#-------------------
#-------------------
