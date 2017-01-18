# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 21:52:32 2016

@author: nimselsa
"""

def find_max_min(list):
    
    x =max(list)
    y =min(list)
    
    if x == y:
        return len(list)
    else:
        return x, y
        
    print(find_max_min(4, 4, 4, 4))
            


        