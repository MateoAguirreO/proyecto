# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:04:54 2019

@author: Mateo A
"""

from Node import Node
import json
import os


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

    def preOrder(self):
        if(self.root):
            nodeList = []
            nodeList = self._preOrder(self.root, nodeList)

            return nodeList
        else:
            print("Empty Tree")

    def _preOrder(self, node, preList):
        preList.append(node)

        if(node.hasLeftChild()):
            self._preOrder(node.getLeftChild(), preList)

        if(node.hasRightChild()):
            self._preOrder(node.getRightChild(), preList)

        return preList

    def inOrder(self):
        if(self.root):
            inNodeList=[]
            inNodeList=self._inOrder(self.root, inNodeList)
            return inNodeList
        else:
            print("Empty Tree")

    def _inOrder(self, node, inList):
        if(node.hasLeftChild()):
            self._inOrder(node.getLeftChild(), inList)
        inList.append(node)
        if(node.hasRightChild()):
            self._inOrder(node.getRightChild(), inList)

        return inList

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

    def width(self):
        if(self.root):
            widthList=[]
            widthList=self._width(self.root, widthList)
            return widthList
        else:
            print(">Empty Tree")

    def _width(self, node, widthList):
        listTmp=[]
        nodeTmp=None
        listTmp.append(node)
        while len(listTmp) > 0:
            nodeTmp = listTmp.pop(0)
            widthList.append(nodeTmp)
            if(nodeTmp.hasLeftChild()):
                listTmp.append(nodeTmp.getLeftChild())
            if(nodeTmp.hasRightChild()):
                listTmp.append(nodeTmp.getRightChild())

        return widthList

    def getListPoints(self):
        """
        Returns a list of dictionaries, that contain points, from a JSON file in 'filePath'.
        """

        filePath = "data.json"

        with open(filePath, "r") as db:
            dbString = db.read()

        parsedData = json.loads(dbString)

        return parsedData["data"]

    def deleteNode(self, label):
        filePath = "data.json"

        with open(filePath, "r") as db:
            dbString = db.read()

        parsedData = json.loads(dbString)

        for node in parsedData["data"]:
            if(node["label"] == label):
                parsedData["data"].remove(node)

        os.remove(filePath)

        with open(filePath, 'w') as db:
            json.dump(parsedData, db, indent=4)

        print("Node deleted succesfully!")

    def modifyNode(self, label, x, y):
        filePath = "data.json"

        with open(filePath, "r") as db:
            dbString = db.read()

        parsedData = json.loads(dbString)

        for node in parsedData["data"]:
            if(node["label"] == label):
                pos = parsedData["data"].index(node)
                parsedData["data"][pos]["x"] = x
                parsedData["data"][pos]["y"] = y

        os.remove(filePath)

        with open(filePath, 'w') as db:
            json.dump(parsedData, db, indent=4)

        print("Node modified succesfully!")

myData = Data()
points = myData.getListPoints()

l = myData.preOrder()

for n in l:
    print(n.getLabel(), ": ", [n.getValueX(), n.getValueY()], " lvl: ", myData.getNodeLevel(n))
