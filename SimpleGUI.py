from PIL import Image
from PIL.ExifTags import TAGS
import glob
from Images import *
from Filter import *
import os,sys
from Archive import *
from Tkinter import *
import tkFileDialog


class App:
    def __init__(self, master):
        
        self.root=master
        
        frame = Frame(master)
        frame.grid()
        master.title("Photot Archiving Wizard")
        
        """select File button"""
        self.fileButton = Button(frame, text="File", command=self.selectFile)
        self.fileButton.grid(row=0,sticky=W)
        
        """Display Label"""
        self.output = StringVar()
        self.display = Label(frame, textvariable=self.output, anchor=W, justify=LEFT,padx=3,pady=3)
        self.output.set("Please select a Directory")
        self.display.grid(row=0,column=1)
        
        """Scene Archive button"""
        self.ScenButton = Button(frame, text="Scene Archive", command=self.goSceneArchive)
        self.ScenButton.grid(row=1,sticky=W)

        """Filter option list"""
        self.filter = StringVar(frame)
        self.filter.set("FocalLength")
        self.filtOption = OptionMenu(frame, self.filter, "FocalLength", "DateTime", "FNumber", "ApertureValue","Model","Software")
        self.filtOption.grid(row=2,sticky=W)
        
        """filter button"""
        self.filtButton = Button(frame, text="Filter", command=self.goFilter)
        self.filtButton.grid(row=3,sticky=W+N)

        """archive option list"""
        self.archive = StringVar(frame)
        self.archive.set("FocalLength")
        self.archOption = OptionMenu(frame, self.archive, "FocalLength", "DateTime", "FNumber", "ApertureValue","Model","Software")
        self.archOption.grid(row=4,sticky=W)
        
        """archive button"""
        self.archButton = Button(frame, text="Archive", command=self.goArchive)
        self.archButton.grid(row=5,sticky=W+N)
    
        """dearchive button"""
        self.ReleButton = Button(frame, text="Release", command=self.goRelease)
        self.ReleButton.grid(row=6, column=0,sticky=W)
        
        """Exit button"""
        self.quitButton = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.quitButton.grid(row=6, column=1,sticky=E)
        
    
    """read all images in the folder"""
    def initailization(self):
        """read all jpg files"""
        os.chdir(self.folder)
        files = glob.glob("*.jpg")
        images = []
    
        """create individual image classes"""
        for i in range(0,len(files)):
            images.append(Images(files[i]))
        return images

    """File button helper"""
    def selectFile(self):
        dirname = tkFileDialog.askdirectory(parent=self.root,initialdir="/",title='Please select a directory')
        if len(dirname ) > 0:
            self.folder = dirname
        self.ims = self.initailization()
        self.printAll(self.ims)
    
    """Print all images on label"""
    def printAll(self,ims):
        text = str(self.folder)+'\n'
        text += "Images detected\n"
        for i in range(0,len(ims)):
            text += ims[i].name + '\n'
            if(ims[i].dir != ''):
                text += '('+ims[i].dir+')' +'\n'
        self.output.set(text)
    
    """Archive button helper"""
    def goArchive(self):
        text = str(self.folder)+'\n'
        newArchive = Archive(self.ims,self.archive.get(),self.folder)
        newArchive.autoArchive()
        for i in range(0,len(newArchive.dirs)):
            text+=' -'+str(newArchive.dirs[i])+'\n'
        self.output.set(text)
        
    
    """Filter button helper"""
    def goFilter(self):
        text = self.filter.get()+'\n'
        newView = Filter(self.ims,self.filter.get())
        text = newView.view()
        self.output.set(text)
    
    """dearchive button helper"""
    def goRelease(self):
        newArchive = Archive(self.ims,'',self.folder)
        newArchive.deArchive()
        self.output.set(str(self.folder)+'\n'+'released')
    
    """Scene archive button helper"""
    def goSceneArchive(self):
        self.output.set('Scene Archiving...')
        newArchive = Archive(self.ims,'',self.folder)
        newArchive.sceneArchive()
        self.output.set(str(self.folder)+'\n'+'Scene Archiving Result:\n'+str(len(newArchive.dirs))+' scenes')
