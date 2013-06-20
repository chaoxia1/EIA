from Images import *
import os
import shutil
from PIL import Image
import numpy
from scipy.linalg import svd

class Archive:
    """All directories for current archiving"""
    dirs = []
    
    """Field to filter on"""
    field = ''
    
    images = []
    
    """old archiving directories"""
    dirToRemove = []
    
    
          
    def __init__(self,im,f,folder):
        self.field = f
        self.images = im
        self.dirToRemove = []
        self.dirs = []
        self.dirname = folder
    
    def create_dir(self,myPath):
        if not os.path.isdir(self.dirname+myPath):
            os.makedirs(self.dirname+'/'+myPath)
 
    def removeDirs(self):
        for i in range(0,len(self.dirToRemove)):
            shutil.rmtree(self.dirname+'/'+self.dirToRemove[i])
    
    """Tasks: 1.Physically move files to new directories  
              2.push old directories to dirToRemove
              3.set individual image directories to the new one
        parameter(k): the k-th new directories
    """
    def moveFiles(self,myPath,k):       
        for i in range(0,len(self.images)):
            if(self.images[i].getValue(self.field) == self.dirs[k]):
                """Push info to dirToRemove"""
                if(self.images[i].dir != '' and self.images[i].dir not in self.dirToRemove):
                    self.dirToRemove.append(self.images[i].dir)
                """move files"""
                if(self.images[i].dir == ''):
                    shutil.move(self.images[i].name,self.dirname+'/'+myPath)
                else:
                    shutil.move(self.images[i].dir + '/' + self.images[i].name,self.dirname+'/'+myPath)
                """set image to the new directory"""
                self.images[i].setDir(myPath)

                
    """Tasks: 1. create new directories
              2. find images and move to new directories
              3. delete old directories
    """    
    def autoArchive(self):
        """auto-creating new directories based on filed specified"""
        for i in range(0,len(self.images)):
            if(self.images[i].getValue(self.field) not in self.dirs):
                self.dirs.append(self.images[i].getValue(self.field))
        
        """Move files while creating new directories"""
        for i in range(0,len(self.dirs)):
            myPath = self.field + ' ' + str(self.dirs[i])
            self.create_dir(myPath)
            self.moveFiles(myPath,i)
        
        """remove old directories"""
        if(len(self.dirToRemove)>0):
            self.removeDirs()

    """release archived images to the root"""
    def deArchive(self):
      for i in range (0,len(self.images)):
        if(self.images[i].dir != ''):
          if(self.images[i].dir not in self.dirToRemove):
            self.dirToRemove.append(self.images[i].dir)
          shutil.move(self.images[i].dir + '/' + self.images[i].name,self.dirname)
          self.images[i].dir = ''
      self.removeDirs()

    """Use SVD to classify scenes"""
    def getRGB(self,k):
      im = self.images[k].im
      im.load()
      r, g, b = im.split()
      (w,h) = im.size
      R = numpy.array(r.getdata())
      R = R.reshape(w,h)
      G = numpy.array(g.getdata())
      G = G.reshape(w,h)
      B = numpy.array(b.getdata())
      B = B.reshape(w,h)
      n = 500
      Ur, Sr, VrT = svd(R.T, full_matrices=False)
      Ug, Sg, VgT = svd(G.T, full_matrices=False)
      Ub, Sb, VbT = svd(B.T, full_matrices=False)
      Sr = Sr[0:n]
      Sg = Sg[0:n]
      Sb = Sb[0:n]
      return Sr,Sg,Sb

    """get average errors"""
    def getError(self,s1,s2):
      error = 0
      for i in range (0,500):
        error += abs(s1[i]-s2[i])/s1[i]
      return error/500
    
    """calculate percent errors"""
    def findScenes(self):
      scene = []
      selected = []
      for i in range(0,len(self.images)):
        if(i not in selected):
          scene.append([])
          scene[len(scene)-1].append(i)
          sr1,sg1,sb1 = self.getRGB(i)
          for j in range(i+1,len(self.images)):
            if(j not in selected):
              sr2,sg2,sb2 = self.getRGB(j)
              er= self.getError(sr1,sr2)
              eg= self.getError(sg1,sg2)
              eb= self.getError(sb1,sb2)
              error = (er+eg+eb)/3
              print i,j,error
              if(error<0.1):
                scene[len(scene)-1].append(j)
                selected.append(j)
      return scene

    
    def sceneArchive(self):
      self.dirToRemove = []
      self.dirs = []
      """filter images by scene"""
      scene = self.findScenes()
      """create new Directories in an array"""
      for i in range(0,len(scene)):
        self.dirs.append("scene"+str(i))
      """move files and creating directories"""
      for i in range(0,len(self.dirs)):
        self.create_dir(self.dirs[i])
        for j in range(0,len(scene[i])):
          if(self.images[scene[i][j]].dir != '' and self.images[scene[i][j]].dir not in self.dirToRemove):
            self.dirToRemove.append(self.images[scene[i][j]].dir)
          if(self.images[scene[i][j]].dir == ''):
            shutil.move(self.images[scene[i][j]].name,self.dirname+'/'+self.dirs[i])
          else:
            shutil.move(self.dirname+self.images[scene[i][j]].dir + '/' + self.images[scene[i][j]].name,self.dirname+'/'+self.dirs[i])
          self.images[scene[i][j]].setDir(self.dirs[i])
      if(len(self.dirToRemove)>0):
        self.removeDirs()




