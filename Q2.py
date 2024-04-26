#!/usr/bin/env python

class Rectangle:
    length = 0
    width = 0

    def __init__(self, length, width):
        self.length = length 
        self.width = width
        
    
    def getArea(self):
      return self.length * self.width  
    
    rectangleOne = Rectangle(4, 3)

    areaofRectangleOne = rectangleOne.getArea()

    print(areaofRectangleOne)