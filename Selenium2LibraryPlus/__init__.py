import os

from Selenium2Library import Selenium2Library
from keywords import *

class Selenium2LibraryPlus(Selenium2Library, _ElementKeyWordsPlus):
    """docstring for Selenium2LibraryPlus"""
    def __init__(self):
        for base in Selenium2LibraryPlus.__bases__:
            base.__init__(self)
        #self.arg = arg
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

if __name__ == '__main__':
	a=Selenium2LibraryPlus
	print a.__bases__