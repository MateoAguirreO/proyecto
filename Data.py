# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:04:54 2019

@author: Mateo A
"""

from Node import Node
import json


class Data:
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


'''def agregar(self, n, dato):
    if not n is None:
        if dato < n.dato:
            if n.izq is None:
                n.izq = Nodo(dato)
            else:
                self.agregar(n.izq, dato)
        if dato > n.dato:
            if n.der is None:
                n.der = Nodo(dato)
            else:
                self.agregar(n.der, dato)

def inOrder(self, n):
    if not n is None:
        self.inOrder(n.izq)
        print(n.dato, end=" ")
        self.inOrder(n.der)

def preOrder(self, n):
    if not n is None:
        print(n.dato, end=" ")
        self.preOrder(n.izq)
        self.preOrder(n.der)

def postOrder(self, n):
    if not n is None:
        self.postOrder(n.izq)
        self.postOrder(n.der)
        print(n.dato, end=" ")

def anchura(self, n):
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

def peso(self, n):
    if n is None:
        return 0
    else:
        return self.peso(n.izq) + self.peso(n.der) + 1

def altura(self, n):
    if n is None:
        return 0
    else:
        max(self.altura(n.izq)+1, self.altura(n.der)+1)

def hojas(self, n):
    if n is None:
        return
    if n is not None:
        if n.izq is None and n.der is None and n.dato is not None:
            print(n.dato)
        self.hojas(n.izq)
        self.hojas(n.der)

def mramas(self, n, lst):
    if not n is None:
        lst.append(n.dato)
        if n.izq is None and n.der is None:
            print(lst)
            lst.pop()
        else:
            self.mramas(n.izq, lst)
            self.mramas(n.der, lst)
            lst.pop()

def aob(self, n, lst):
    if n is not None:
        lst.append(n.dato)
        self.aob(n.izq, lst)
        self.aob(n.der, lst)
    return lst

def taob(self, lista, i):
    if len(lista) > 1:
        m = lista[i]
        if lista[i-1] > lista[i]:
            print("no es ordenado")
        else:
            if i < len(lista):
                taob(lista, i+1)
    else:
        print("no es ordenado")

def addfibo(self, n):
    if not n is None:
        if dato < n.dato:
            if n.izq is None:
                n.izq = Nodo(dato)
            else:
                self.agregar(n.izq, dato)
        if dato > n.dato:
            if n.der is None:
                n.der = Nodo(dato)
            else:
                self.agregar(n.der, dato)'''
