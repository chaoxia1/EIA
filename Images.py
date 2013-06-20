from PIL import Image
from PIL.ExifTags import TAGS

class Images:
    name = ''
    exif = {}
    
    """an image instance for more filtering options"""
    im = ''
    
    """current directory"""
    dir = ''
    
    """
    Tasks: Read all Exif of one image
    Return: A dictionary of Exif
    """
    def get_exif(self):
        ret = {}
        i = Image.open(self.name)
        info = i._getexif()
        """store the information in a dictionary"""
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
        return ret

    def __init__(self,n):
        self.name = n
        self.exif = self.get_exif()
        self.im = Image.open(self.name)
    
    def getValue(self,field):
        return self.exif[field]
    
    def setDir(self,dirName):
        self.dir = dirName
        
    
    
    
    
    
    
