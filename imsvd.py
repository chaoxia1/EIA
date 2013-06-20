from math import sin, cos, pi, factorial ;
import numpy
from PIL import Image
from scipy.linalg import svd
from matplotlib.pylab import show,figure,plot


def taskOne():
  im = Image.open("lake.tif")
  im.load()
  """im.show()"""
  return im


def taskThreeAndFour(R,G,B,w,h):
  """Task Three"""
  Ur, Sr, VrT = svd(R.T, full_matrices=False)
  Ug, Sg, VgT = svd(G.T, full_matrices=False)
  Ub, Sb, VbT = svd(B.T, full_matrices=False)

  """Task Seven"""
  taskSeven(Sr,Sg,Sb)
    
  """Task Four"""
  newim = Image.new('RGB',(w,h))
  R = numpy.dot(numpy.dot(Ur,numpy.diag(Sr)),VrT)
  R = numpy.array(R.T.flatten(),dtype=int)
  G = numpy.dot(numpy.dot(Ug,numpy.diag(Sg)),VgT)
  G = numpy.array(G.T.flatten(),dtype=int)
  B = numpy.dot(numpy.dot(Ub,numpy.diag(Sb)),VbT)
  B = numpy.array(B.T.flatten(),dtype=int)
  t = zip(R,G,B)
  newim.putdata(t)
  """newim.show()"""
  """newim.save("svdreconstruct.tif")"""


def taskFive(n,R,G,B,w,h):
  Ur, Sr, VrT = svd(R.T, full_matrices=False)
  Ug, Sg, VgT = svd(G.T, full_matrices=False)
  Ub, Sb, VbT = svd(B.T, full_matrices=False)
  Ur = Ur[:,0:n]
  Sr = Sr[0:n]
  VrT = VrT[0:n,:]
  Ug = Ug[:,0:n]
  Sg = Sg[0:n]
  VgT = VgT[0:n,:]
  Ub = Ub[:,0:n]
  Sb = Sb[0:n]
  VbT = VbT[0:n,:]

  newim = Image.new('RGB',(w,h))
  R = numpy.dot(numpy.dot(Ur,numpy.diag(Sr)),VrT)
  R = numpy.array(R.T.flatten(),dtype=int)
  G = numpy.dot(numpy.dot(Ug,numpy.diag(Sg)),VgT)
  G = numpy.array(G.T.flatten(),dtype=int)
  B = numpy.dot(numpy.dot(Ub,numpy.diag(Sb)),VbT)
  B = numpy.array(B.T.flatten(),dtype=int)
  t = zip(R,G,B)
  newim.putdata(t)
  """newim.show()"""
  newim.save("large"+str(n)+".tif")

def taskSix(n,R,G,B,w,h):
    Ur, Sr, VrT = svd(R.T, full_matrices=False)
    Ug, Sg, VgT = svd(G.T, full_matrices=False)
    Ub, Sb, VbT = svd(B.T, full_matrices=False)
    Ur = Ur[:,(374-n):374]
    Sr = Sr[(374-n):374]
    VrT = VrT[(374-n):374,:]
    Ug = Ug[:,(374-n):374]
    Sg = Sg[(374-n):374]
    VgT = VgT[374-n:374,:]
    Ub = Ub[:,(374-n):374]
    Sb = Sb[(374-n):374]
    VbT = VbT[(374-n):374,:]
    newim = Image.new('RGB',(w,h))
    R = numpy.dot(numpy.dot(Ur,numpy.diag(Sr)),VrT)
    R = numpy.array(R.T.flatten(),dtype=int)
    G = numpy.dot(numpy.dot(Ug,numpy.diag(Sg)),VgT)
    G = numpy.array(G.T.flatten(),dtype=int)
    B = numpy.dot(numpy.dot(Ub,numpy.diag(Sb)),VbT)
    B = numpy.array(B.T.flatten(),dtype=int)
    t = zip(R,G,B)
    newim.putdata(t)
    """newim.show()"""
    newim.save("small"+str(n)+".tif")
    

def taskSeven(Sr,Sg,Sb):
  x = numpy.linspace(1,375,375)
  figure()
  plot(x,Sr,'r')
  plot(x,Sg,'g')
  plot(x,Sb,'b')
  show()
  print Sr[0:9]



def main():
  """task One"""
  im = taskOne()
    
  """Task Two"""
  r, g, b = im.split()
  (w,h) = im.size
  R = numpy.array(r.getdata())
  R = R.reshape(w,h)
  G = numpy.array(g.getdata())
  G = G.reshape(w,h)
  B = numpy.array(b.getdata())
  B = B.reshape(w,h)

  """Task Three and Four"""
  taskThreeAndFour(R,G,B,w,h)

  """Task Five
  for i in [200,100,50,10,1]:
    taskFive(i,R,G,B,w,h)"""

  """Task Six
  for i in [200,100,50,10,1]:
    taskSix(i,R,G,B,w,h)"""

  
  
  
  
    

if __name__ == "__main__":
  main()
