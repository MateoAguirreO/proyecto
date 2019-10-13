# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:04:54 2019

@author: Mateo A
"""

from Node import Node

class Data:


    # nodeId = eje
    def __init__(self):
        #self.root = Node("x", datox, datoy)
        self.root = None

    def addNodes(self, list):
        for coord in list:
            self.addNode("x", coord[0], coord[1])

    def addNode(self, nodeId, valueX, valueY):
        if(self.root):
            self._addNode(nodeId, valueX, valueY, self.root)
        else:
            self.root = Node(nodeId, valueX, valueY, None)

    def _addNode(self, nodeId, valueX, valueY, parent):
        if(valueY > parent.getValueY()):
            if(parent.getRightChild()):
                self._addNode("x", valueX, valueY, parent.getRightChild())
            else:
                parent.setRightChild(Node("y", valueX, valueY, parent))
        elif(valueY < parent.getValueY()):
            if(parent.getLeftChild()):
                self._addNode("x", valueX, valueY, parent.getLeftChild())
            else:
                parent.setLeftChild(Node("y", valueX, valueY, parent))
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


myData = Data()

myData.addNode("x", 5, 8)
myData.addNode("y", 1, 13)
myData.addNode("y", 10, 15)
myData.addNode("y", 11, 15)
myData.addNode("y", 20, 12)

l = myData.preOrd()

for n in l:
    print([n.getValueX(), n.getValueY()])


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
