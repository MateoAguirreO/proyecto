# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:04:54 2019

@author: Mateo A
"""

from Node import Node
import json


class Data:
    """
    Class to create the BST and manage all the points based in the data.json
    """
    def __init__(self):
        self.root = None
        self.addNodes()

    def getNodeLevel(self, node):
        if(node.parent is None):
            return 0

        return 1 + self.getNodeLevel(node.parent)

    def addNodes(self):
        nodeList = self.getListPoints()

        for point in nodeList:
            self.addNode(point["label"], point["x"], point["y"])

    def addNode(self, label, valueX, valueY):
        if(self.root):
            self._addNode(label, valueX, valueY, self.root)
        else:
            self.root = Node(label, valueX, valueY, None)

    def _addNode(self, label, valueX, valueY, parent):
        # Compare if the parent level is odd to know what component compare
        if(self.getNodeLevel(parent) % 2 == 0):
            # Compare the valueX param with the parent valueX
            if(valueX > parent.getValueX()):
                if(parent.getRightChild()):
                    self._addNode(label, valueX, valueY, parent.getRightChild())
                else:
                    parent.setRightChild(Node(label, valueX, valueY, parent))
            elif(valueX < parent.getValueX()):
                if(parent.getLeftChild()):
                    self._addNode(label, valueX, valueY, parent.getLeftChild())
                else:
                    parent.setLeftChild(Node(label, valueX, valueY, parent))
            else:
                print(f"Node {str(valueX)} already exists!")
        else:
            # Compare the valueY param with the parent valueY
            if(valueY > parent.getValueY()):
                if(parent.getRightChild()):
                    self._addNode(label, valueX, valueY, parent.getRightChild())
                else:
                    parent.setRightChild(Node(label, valueX, valueY, parent))
            elif(valueY < parent.getValueY()):
                if(parent.getLeftChild()):
                    self._addNode(label, valueX, valueY, parent.getLeftChild())
                else:
                    parent.setLeftChild(Node(label, valueX, valueY, parent))
            else:
                print(f"Node {str(valueY)} already exists!")

    def preOrd(self):
        if(self.root):
            nodeList = []
            nodeList = self._preOrd(self.root, nodeList)

            return nodeList
        else:
            print("Empty Tree")

    def _preOrd(self, node, preList):
        preList.append(node)

        if(node.hasLeftChild()):
            self._preOrd(node.getLeftChild(), preList)

        if(node.hasRightChild()):
            self._preOrd(node.getRightChild(), preList)

        return preList

    def postOrder(self):
        if(self.root):
            postNodeList=[]
            postNodeList=self._postOrder(self.root, postNodeList)
            return postNodeList
        else:
            print("Empty Tree")

    def _postOrder(self, node, postList):

        if(node.hasLeftChild()):
            self._postOrder(node.getLeftChild(), postList)

        if(node.hasRightChild()):
            self._postOrder(node.getRightChild(), postList)

        postList.append(node)

        return postList



    def inOrder(self):
        if(self.root):
            inNodeList=[]
            inNodeList=self._postOrder(self.root, inNodeList)
            return inNodeList
        else:
            print("Empty Tree")

    def _postOrder(self, node, inList):

        if(node.hasLeftChild()):
            self._postOrder(node.getLeftChild(), inList)

        inList.append(node)

        if(node.hasRightChild()):
            self._postOrder(node.getRightChild(), inList)
        return inList




    '''
    defanchura(self, n):
        if not n is None:
            cola = []
            nodoTmp = None
            cola.append(n)
            while len(cola) > 0:
                nodoTmp = cola.pop(0)
                print(nodoTmp.dato, end = " ")
                if not nodoTmp.izq is None:
                    cola.append(nodoTmp.izq)
                if not nodoTmp.der is None:
                    cola.append(nodoTmp.der)
    '''

    def getListPoints(self):
        """
        Returns a list of dictionaries, that contain points, from a JSON file in 'filePath'.
        """

        filePath = "data.json"

        with open(filePath, "r") as db:
            dbString = db.read()

        parsedData = json.loads(dbString)

        return parsedData["data"]


myData = Data()
points = myData.getListPoints()

l = myData.preOrd()

for n in l:
    print(n.getLabel(), ": ", [n.getValueX(), n.getValueY()], " lvl: ", myData.getNodeLevel(n))
