from PIL import Image
from PIL.ExifTags import TAGS
import glob
from Images import *
from Filter import *
import sys
from Archive import *
from SimpleTestGUI import *
from SimpleGUI import *


"""Tasks: 1.read all image files  
          2.create individual image class
   Return: an array of Images
"""


def main():   
    """simpleTestGUI(allImages)"""
    """simpleGUI(allImages)"""
    root = Tk()
    app = App(root)
    root.mainloop() 
    


if __name__ == '__main__':
    main()