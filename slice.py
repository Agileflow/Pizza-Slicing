# -*- coding: utf-8 -*-

"""
    Slice of a pizza
    A slice must contain at least L number of either of the ingredients
    A slice can contain H max number of either of the ingredients
"""
class Slice:
    # Slice constructor that takes PizzaData type
    # its members are defined private
    def __init__(self, data):
        self.__max = data.getH()    # H max number of either ingredients that a slice can contain
        self.__min = data.getL()    # L min number of either ingredients that must be in a slice
        self.__ingredients = list()   # ingredients in a slice

        
    def addIngredient(self, ingredient):
        if len(self.__ingredients) < self.__max: # check the slice has not exceed the max number of ingredients allowed
            self.__ingredients.append(ingredient) # append new ingredient to the slice
            # return True if ingredient was added to the slice
            return True
        else:
            # return False if slice has reached the allowed number of ingredients
            return False
    
    # return the ingredients of this slice
    def getSlice(self):
        return self.__ingredients
    