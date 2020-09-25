# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:40:22 2020

@author: lenovo

Imagine a robot in a 2D plane. Now it can make a series of moves encoded as 'U', 'D', 'L', 'R' representing
'UP', 'DOWN', 'LEFT', 'RIGHT' respctively. Given an sequence of moves, tell if the robot comes back to where it started from.
Example:
    input: UDLURD
    output: True
    input: UL
    output: False

"""

import timeit as t

def time(f):
    starttime = t.default_timer()
    finishtime = t.default_timer()
    print( finishtime - starttime)



def distancebetmoves(moves):
    x =0
    y = 0
    
    path_1 = moves[0]
    for i in range(len(moves)):
        if moves[i] == "U":
            y +=1
        elif moves[i] =="R":
            x +=1
        elif moves[i] == "L":
            x -=1
        else:
            y -=1
        
    ## checking at end x = 0 and y=0
    if x == 0 and y == 0:
        return True
    else:
        return False
    
m = "UDLURDLL"
result = distancebetmoves(m)
print(result)
    
        
        

