# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:05:48 2019

@author: Mateo A
"""

class Node:
    def __init__(self, id,x,y):
        self.id=id
        self.x=x
        self.y=y
        self.izq=None
        self.der=None
        