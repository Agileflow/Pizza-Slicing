# -*- coding: utf-8 -*-

#3 5 1 6
#TTTTT
#TMMMT
#TTTTT

class PizzaData:
    
    # specifies the output file directory
    __outputDir = 'outputs/'
    
    # PizzaData constructor with parameter 'path'
    # 'path' the containing the input file path, filename and extension
    def __init__(self, path):
        try:
            f = open(path, 'r') # open file in read mode
            self.content = f.readlines() # read file contents into a list delmited by \n
            
            """ 
                remove \n delimiter
                would have effect on overall efficiency when content is large
                Use heuristic to blind indexing to the delimiter 
            """
            self.content = [ line.replace(line[-1],'') for line in self.content ]  
                            
        # catch FileNotFound exception 
        except:
            print('File path "', path, '" specified does not exist') # output only probable error, file path specified
        finally:
            if f != None:
                f.close() # close IO
        
    # Get the pizza total rows as specified in the input file R
    def getTotalRow(self):
        return self.content[0][0]   # content[0][0] specifies the pizza total row
    
    # Get the pizza total columns as specified in the input file C
    def getTotalCol(self):
        return self.content[0][2]   # content[0][2] specifies the pizza total column
    
    # Get min number of each ingredients(cell) expected in a slice L
    def getMinCell(self):
        return self.content[0][4] # content[0][4] specifies the pizza min number of either ingredients expected in a slice
    
    # Get max number of either ingredients(cell) expected in a slice H
    def getMaxCells(self):
        return self.content[0][6] # content[0][6] specifies the max number of ingredients expected in a slice

    def getPizzaIngredients(self):
        k = list(self.content)
        k.pop(0)    # Pop constants/constraints line [R C L H]
        return k # return pizza ingredients R and C
        
    