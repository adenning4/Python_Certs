# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 18:40:24 2022

@author: adenn
"""

class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        area = self.height * self.width
        return area
    
    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter
    
    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** 0.5)
        return diagonal
    
    def get_picture(self):
        if ((self.width > 50) or (self.height > 50)):
            statement = 'Too big for picture.'
            return statement
        picture = ''
        #picture += self.width * '*' + '\n'
        for i in range(self.height):
            #picture += '*' + ((self.width - 2) * '*') + '*\n'
            picture += self.width * '*' + '\n'
        #picture += self.width * '*'
        return picture
    
    def get_amount_inside(self,oshape):
        fitcount = 0
        if (oshape.width > self.width) or (oshape.height > self.height):
            return fitcount
        else:
            fitcount += (self.width//oshape.width)*(self.height//oshape.height)
            return fitcount
        
class Square(Rectangle):
    def __init__(self,side):
        self.side = side
        self.width = side
        self.height = side
        
    def __str__(self):
        return f'Square(side={self.side})'
    
    def set_side(self, side):
        self.__init__(side)
    
    def set_width(self,width):
        self.__init__(width)
    
    def set_height(self,height):
        self.__init__(height)
    
    