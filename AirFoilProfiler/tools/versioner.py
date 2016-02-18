
#-------------------
#-------------------

## @package versioner
#  @authors Celestica's Team
#  @brief Module used to update .py file versions and date
#  @date 26/11/2014
#  @version v1.0
#
#  @details This module is an applications to access .py files and to change data
#   and version information.

#-------------------
#-------------------

import os
import sys
import glob
import shutil
import getopt
from datetime import datetime

#------------------
#----  VERSION ----

MAJOR = '0'
MINOR = '1'
PATCH = '1'
VERSION = MAJOR + '.' + MINOR + '.' + PATCH
PATH = '../src'
PATH_BACKUP = PATH + '/BACKUP'

#------------------
#----  METHODS ----

def printHelp():
    print('Usage: ' + thisFilename + ' -v version -p path(without final backslash) -h help')

#-------------------
#-------------------

## Main Entry
# @details Runs if the program is run directly or
# passed as an argument to the python

if __name__ == "__main__":
    thisPath, thisFilename = os.path.split(os.path.realpath(__file__))
    thisFilenameFields = thisFilename.split('.')
    PATH = thisPath + '/' + PATH
    PATH_BACKUP = PATH + '/BACKUP'

    try:
        myopts, args = getopt.getopt(sys.argv[1:], 'v:p')
    except getopt.GetoptError as e:
        myLogger.write(str(e))
        printHelp()
        sys.exit(1)

    if not os.path.exists(PATH_BACKUP):
        os.makedirs(PATH_BACKUP)

    # o == option
    # a == argument passed to the o
    for o, a in myopts:
        if o == '-h':
            #Print help
            printHelp()
            sys.exit(0)
        elif o == '-v':
            try:
                VERSION = str(a)
                splitted = VERSION.split('.')
                MAJOR = splitted[0]
                MINOR = splitted[1]
                PATCH = splitted[2]
            except:
                print ('Version error')
                sys.exit(2)
        elif o == '-p':
            try:
                PATH = str(a)
            except:
                print ('Path error')
                sys.exit(2)

    fileList = []
    for root, subFolders, files in os.walk(PATH):
        for a in files:
            if '.py' in a and not '.pyc' in a:
                fileList.append(root + '/' + a)
    print ('Updating files ... ')
    for fileName in fileList:
        p,f = os.path.split(fileName)
        if f != thisFilename and f != 'restorerBackup.py':
            print (' -- ' + f)
            try:
                shutil.copy2(fileName, PATH_BACKUP + '/' + f)
                oFile = open(fileName,'r')
                lines = oFile.readlines()
                oFile.close()

                oFile = open(fileName,'w')
                for line in lines:
                    if '@version' in line:
                        line = '#  @version v' + VERSION  + '\n'
                    elif '@date' in line:
                        line = "#  @date " + datetime.now().strftime('%d/%m/%Y') + '\n'
                    elif 'MAJOR =' in line:
                        line = 'MAJOR = str(' + MAJOR + ')\n'
                    elif 'MINOR =' in line:
                        line = 'MINOR = str(' + MINOR + ')\n'
                    elif 'PATCH =' in line:
                        line = 'PATCH = str(' + PATCH + ')\n'
                    oFile.write(line)
                oFile.close()
            except:
                print ('Error editing \"' + fileName + '\" file')
                sys.exit(3)

#-------------------
#-------------------
