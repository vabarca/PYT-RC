
#-------------------
#-------------------

## @package AirFoilsUtils
#  @authors TT
#  @brief Utils for the airfoil project
#  @date 16/02/2016
#  @version v0.1.0
#
#  @details

#-------------------
#-------------------

import os
import sys
import unittest

#------------------
#----  VERSION ----

MAJOR = '0'
MINOR = '1'
PATCH = '0'

VERSION = MAJOR + '.' + MINOR + '.' + PATCH

#------------------
#--  CONSTANTS ----

_DEBUG = 0

#------------------
#----  METHODS ----

## checks if a value is a float
#
# @details Checks if the value param is a float number
#  @param value to evaluate
#  @return true if float or false if not
def isfloat(value):
    try:
        float(value)
        return True
    except:
        return False

## getFiles from folder and subfolders
#
# @details This method returs all files from the
#  rootdir folder and subfolders
#  @param rootdir folder to be analized.
#  @return file's path list
def getFiles(rootdir):
    Rslt = []
    for root, subFolders, files in os.walk(rootdir):
        for a in files:
            Rslt.append(root + '/' + a)
    return Rslt

## Filters the given list
#
# @details This method filters the string list wich elements
#  match with the pattern
#  @param rootdir folder to be analized.
#  @return file's path list
def filterList(strlist,pattern):
    Rslt = []
    if type(pattern) is str:
        for a in strlist:
            if type(a) is str:
                if pattern in a:
                    Rslt.append(a)
    return Rslt

## Creates folder
#
# @details This method creates the given folder
#  @param strFolder folder name
#  @param bDelete indicates if delete content is required
def createFolder(strFolder, bDelete = False):
    if os.path.exists(strFolder):
        if bDelete:
            for a in getFiles(strFolder):
                os.remove(a)
    else:
        os.makedirs(strFolder)

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

    def test_A(self):
        self.assertTrue(isfloat(1.18))
        self.assertFalse(isfloat(""))

#------------------
#------  MAIN -----

## Main Entry
# @details If the program is run directly or passed as an argument to the python
#  interpreter then create a tiny Mintaka Server
if __name__ == "__main__":
    unittest.main()

#------------------
#------------------
