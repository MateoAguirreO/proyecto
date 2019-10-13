# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:05:48 2019

@author: Mateo A
"""


class Node:
    def __init__(self, label, valueX, valueY, parent):
        self.label = label
        self.valueX = valueX
        self.valueY = valueY
        self.parent = parent
        self.leftChild = None
        self.rightChild = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getValueX(self):
        return self.valueX

    def getValueY(self):
        return self.valueY

    def setValueX(self, valueX):
        self.valueX = valueX

    def setValueY(self, valueY):
        self.valueY = valueY

    def hasLeftChild(self):
        if(self.leftChild):
            return True
        return False
    
    def getLeftChild(self):
        return self.leftChild
    
    def setLeftChild(self, leftC):
        self.leftChild = leftC
    
    def hasRightChild(self):
        if(self.rightChild):
            return True

    def getRightChild(self):
        return self.rightChild

    def setRightChild(self, rightC):
        self.rightChild = rightC

    def getParent(self):
        return self.parent

    def setParent(self, p):
        self.parent = p

    def isLeaf(self):
        return (not self.leftChild and not self.rightChild)

    def isRightChild(self):
        return (self.getParent().hasRightChild() and self.value == self.parent.rightChild.value)

    def isLeftChild(self):
        return (self.getParent().hasLeftChild() and self.value == self.parent.leftChild.value)

    def hasGrandPa(self):
        if(self.parent.parent is not None):
            return True
        return False

    def getGrandPa(self):
        return self.parent.parent

    def isRoot(self):
        return (self.parent is None)
