# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 20:48:25 2022

@author: adenn
"""

import copy
import random

class Hat:
    def __init__(self,**balls):
        contents = []
        for key in dict(**balls).keys():
            for i in range(dict(**balls)[key]):
                contents.append(key)
        self.contents = contents

    def draw(self,number):
        result=[]
        
        #how to draw if not drawing more than number in the hat
        if number < len(self.contents):
            for i in range(number):
                result.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
        
        #if drawing the full amount, or more, just give the contents back
        else:
            result = self.contents
            #empty hat!
            self.contents = []
        return result     

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m=0
    for i in range(num_experiments):
        #generate a copy to perform the operation on
        #changes to the deepcopy do not change the original
        #regenerate the copy each time the experiment is performed
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        check = []
        for key in expected_balls.keys():
            #check if the drawn color occurs same or more than the expected
            if expected_balls[key] <= balls_drawn.count(key):
                check.append(False)
            else:
                check.append(True)
            #count how many times the expected result happened
        if not any(check):
            m += 1
        
    probability = m/num_experiments
    return probability
                
    
hat1 = Hat(yellow = 2, red = 3, blue = 5)
expected_balls = {'yellow':1,'red':1,'blue':1}
num_balls_drawn = 7
num_experiments = 10000

result = experiment(hat1,expected_balls,num_balls_drawn,num_experiments)
print(result)