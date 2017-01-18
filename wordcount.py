# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 18:43:01 2017

@author: nimselsa
"""

def words(s):
    word_string = s.split()
    
    word_dict={}
    
    for word in word_string:
        if word.isnumber():
            word = int(word)
        if word in word_dict:
            word_dict[word]+= 1
        else:
            word_dict[word] = 1
            
            print(word_dict)
   
    
    
    