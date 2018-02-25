# -*- coding: utf-8 -*-
"""
    Ingredients contained in a pizza
    Pizza represented as a rectangle represent 2-dimensional
"""

# Ingredient of a pizza
class Ingredient:
    
    # Ingredient constructor with row and col of the ingredient on the pizza
    def __init__(self, row, col, ingredient):
        self.__r = row      # row of the ingredient
        self.__c = col      # column of the ingredient
        self.__i = ingredient   # ingredients( Tomatoe or Mushroom)
    
    # Get index(row, column) of the ingredient on the pizza
    def getIndex(self):
        return self.__r, self.__c   # return row and column of ingrdient
    
    # Get ingredient
    def getIngredient(self):
        return self.__i
