from Images import *

class Filter:
    images = []
    
    """filed to filter"""
    field = ''
    
    """filter titles"""
    filters = []
    
    def __init__(self,i,f):
        self.images = i
        self.field = f
    
    """Tasks: 1. auto-creating view based on field specified
              2. print out the view
    """
    def view(self):
        """find filters titles"""
        self.filters = []
        for i in range(0,len(self.images)):
            if(self.images[i].getValue(self.field) not in self.filters):
                self.filters.append(self.images[i].getValue(self.field))
                
        text =  "Filter by " + self.field +'\n'
        """print out the view"""
        for i in range(0,len(self.filters)):
            text+= str(self.filters[i])+" : \n"
            for j in range(0,len(self.images)):
                if(self.images[j].getValue(self.field) == self.filters[i]):
                    text+= self.images[j].name+'\n'
        return text
                         