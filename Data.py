# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:04:54 2019

@author: Mateo A
"""
from Node import Node

class Data:
    '''id= eje '''
    raiz=None
    def __init__(self, datox, datoy):
        self.raiz=Node("x", datox, datoy)
    
    def agregar(self, n, datox, datoy, id):
        
        if not n is None:
            if id is None:
                if datoy<n.y:
                    if n.izq is None:
                        n.izq=Node("y",datox, datoy)
                    else:
                        self.agregar(n.izq, datox, datoy,"x")
                if datoy>n.y:
                    if n.der is None:
                        n.der=Node("y",datox, datoy)
                    else:
                        self.agregar(n.izq, datox, datoy,"x")
                    
        
        
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
    
