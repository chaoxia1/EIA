from PIL import Image
from PIL.ExifTags import TAGS
import glob
from Images import *
from Filter import *
import os,sys
from Archive import *


def printAll(ims):
    print "Images detected"
    for i in range(0,len(ims)):
        print ims[i].name
        if(ims[i].dir != ''):
            print '(',ims[i].dir,')'
        
        
def simpleFilterTest(ims):
    printAll(ims)
    print "1.filter by FocalLength"
    print "2.filter by DateTime"
    
    f = input("Enter #: ")
    if(f == 1):
        newView = Filter(ims,'FocalLength')
        newView.view()
    elif(f == 2):
        newView = Filter(ims,'DateTime')
        newView.view()
        
def simpleArchiveTest(ims):
    printAll(ims)
    print "1.Archive by FocalLength"
    print "2.Archive by DateTime"
    print "3.Release"
    print "4.Scene Archive"
    
    f = input("Enter #: ")
    if(f == 1):
        newArchive = Archive(ims,'FocalLength')
        newArchive.autoArchive()
    elif(f == 2):
        newArchive = Archive(ims,'DateTime')
        newArchive.autoArchive()
    elif(f == 3):
	newArchive = Archive(ims,'')
        newArchive.deArchive()
    elif(f == 4):
        newArchive = Archive(ims,'')
        newArchive.sceneArchive()
        
def simpleTestGUI(ims):
    yn = "yes"
    while(yn == "yes"):
        print "1: filter test"
        print "2: Archiving test"
        f = input("Enter #: ")
        if(f == 1):
            simpleFilterTest(ims)
        else:
            simpleArchiveTest(ims)       
        yn = raw_input("Keep testing?")
    
    
