# -*- coding: utf-8 -*-
"""
@author: Parjua
"""


import tkinter as tk
from PIL import Image, ImageTk
from random import choice
import generateGraph
import Data
import generate3D


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("700x500")
        self.pack()
        self.createWidgets()
        self.canvas = None
        self.colours = ["#ffe7ad", "#db75c5", "#a05f96", "#ffafb0", "#5eb7b7", "#b673e2", "#96d1c7", "#fc7978", "#edb5f5"]
        self.chargeData()
        self.i = 4

    def chargeData(self):
        self.tree = Data.Data()
        self.treeWeight = len(self.tree.preOrder())
        self.type = self.chooseBest()
        self.graph = generateGraph.Graph(self.tree, self.type)
        self.graph.setGraph()
        self.rectangles = self.graph.getRectangles()
        self.sumRectangles = len(self.rectangles)
        self.labels = [None] * self.sumRectangles
        self.model3d= generate3D.Model3d(self.rectangles)

    def show3D(self):
        self.model3d.getPlt().show()

    def createWidgets(self):
        self.btnNextGraph = tk.Button(self)
        self.btnNextGraph["text"] = "> Next"
        self.btnNextGraph["command"] = self.nextGraph
        self.btnNextGraph.pack(side="top")

        self.btnWindowCanvas = tk.Button(self)
        self.btnWindowCanvas["text"] = "See Map"
        self.btnWindowCanvas["command"] = self.windowCanvas
        self.btnWindowCanvas.pack(side="top")

        self.btnShowAlternatives = tk.Button(self)
        self.btnShowAlternatives["text"] = "Show Alternatives"
        self.btnShowAlternatives["command"] = self.showAlternatives
        self.btnShowAlternatives.pack(side="top")

        self.btnQuit = tk.Button(self, text="See 3D Graph", command=self.show3D)
        self.btnQuit.pack(side="top")

        self.btnModifyPoint = tk.Button(self)
        self.btnModifyPoint["text"] = "Modify Node"
        self.btnModifyPoint["command"] = self.modifyPoint
        self.btnModifyPoint.pack(side="top")

        self.btnModifyPoint = tk.Button(self)
        self.btnModifyPoint["text"] = "Delete Node"
        self.btnModifyPoint["command"] = self.deletePoint
        self.btnModifyPoint.pack(side="top")

        self.btnQuit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.btnQuit.pack(side="bottom")

    def modifyPoint(self):
        window = tk.Toplevel(self.master)
        labelPoint = tk.Label(window, text='Ingresa el label del punto: ')
        labelPoint.pack()

        entryLabel = tk.Entry(window)
        entryLabel.pack()

        valueX = tk.Label(window, text='Ingresa el valor X del punto: ')
        valueX.pack()

        entryValueX = tk.Entry(window)
        entryValueX.pack()

        valueY = tk.Label(window, text='Ingresa el valor Y del punto: ')
        valueY.pack()

        entryValueY = tk.Entry(window)
        entryValueY.pack()

        btnChange = tk.Button(window, text='Change!', command=lambda: self.changePoint(entryLabel.get(), entryValueX.get(), entryValueY.get()))
        btnChange.pack()

    def deletePoint(self):
        window = tk.Toplevel(self.master)
        labelPoint = tk.Label(window, text='Ingresa el label del punto: ')
        labelPoint.pack()

        entryLabel = tk.Entry(window)
        entryLabel.pack()

        btnChange = tk.Button(window, text='Delete!', command=lambda: self._deletePoint(entryLabel.get()))
        btnChange.pack()

    def _deletePoint(self, label):
        self.tree.deleteNode(label)
        super().__init__(self.master)

    def changePoint(self, label, x, y):
        self.tree.modifyNode(str(label), int(x), int(y))
        self.chargeData()

    def showAlternatives(self):
        window = tk.Toplevel(self.master)
        canvas = tk.Canvas(window, width=1080, height=900)
        canvas.pack()

        imgPre = Image.open("img/pre"+str(self.treeWeight+3)+".png")
        imagePre = ImageTk.PhotoImage(imgPre.resize((512, 384)))
        canvas.create_image(250, 160, image=imagePre)

        imgIn = Image.open("img/in"+str(self.treeWeight+3)+".png")
        imageIn = ImageTk.PhotoImage(imgIn.resize((512, 384)))
        canvas.create_image(800, 160, image=imageIn)

        imgPost = Image.open("img/post"+str(self.treeWeight+3)+".png")
        imagePost = ImageTk.PhotoImage(imgPost.resize((512, 384)))
        canvas.create_image(500, 530, image=imagePost)

        canvas.create_image(image=imagePost)

    def windowCanvas(self):
        window = tk.Toplevel(self.master)
        canvas = tk.Canvas(window, width=500, height=500)
        canvas.pack()
        i = 0

        for rectangle in self.rectangles:
            x1, y1 = rectangle[0]
            x2, y2 = rectangle[1]
            tag = "rectangle"+str(i)

            newRectangle = canvas.create_rectangle(x1*20, (25-y1)*20, x2*20, (25-y2)*20, fill=choice(self.colours), tags=tag)

            # Change the rectangle colour when right click is pressed
            canvas.tag_bind(tag, "<Button-3>", lambda event: self.changeColor(event))
            # Create a label in the rectangle when double-left click is pressed
            canvas.tag_bind(tag, "<Double-1>", lambda event: self.getLabel(event))
            i += 1

    def changeColor(self, event):
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)

        eventRectangle = canvas.find_closest(x,y)

        canvas.itemconfig(eventRectangle, fill=choice(self.colours))

    def createLabel(self, event, userText, window):
        window.destroy()
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)

        eventRectangle = canvas.find_closest(x,y)
        coordsRectangle = canvas.coords(eventRectangle)

        if(self.labels[eventRectangle[0]] == None):
            labelRectangle = tk.Label(canvas, text=userText)
            labelRectangle.place(x=coordsRectangle[0]+7, y=coordsRectangle[1]+10)
            self.labels[eventRectangle[0]] = 1

    def getLabel(self, event):
        window = tk.Toplevel(self.master)
        labelPoint = tk.Label(window, text='Ingresa el label del rectangulo: ')
        labelPoint.pack()

        entryLabel = tk.Entry(window)
        entryLabel.pack()

        btnChange = tk.Button(window, text='Submit', command=lambda: self.createLabel(event, entryLabel.get(), window))
        btnChange.pack()

    def createCanvas(self):
        self.canvas = tk.Canvas(self.master, width=700, height=400)
        self.canvas.pack()

    def nextGraph(self):
        if(self.canvas):
            if(self.i >= self.treeWeight + 4):
                self.i = 4
            img1 = Image.open("img/"+self.type+str(self.i)+".png")
            self.image = ImageTk.PhotoImage(img1.resize((512, 384)))
            self.canvas.create_image(350, 200, image=self.image)
            self.i += 1
        else:
            self.createCanvas()
            self.nextGraph()

    def getRectangleArea(self, rectangle):
        x1, y1 = rectangle[0]
        x2, y2 = rectangle[1]

        area = (x2 - x1) * (y1 - y2)

        return area

    def getSmallerArea(self, rectanglesList):
        # smaller = self.graph.maxValue**2
        smaller = 25**2

        for rectangle in rectanglesList:
            area = self.getRectangleArea(rectangle)

            if(area < smaller):
                smaller = area

        return smaller

    def chooseBest(self):
        graphs = []
        smallersList = []

        graphs.append(generateGraph.Graph(self.tree, "pre"))
        graphs.append(generateGraph.Graph(self.tree, "in"))
        graphs.append(generateGraph.Graph(self.tree, "post"))

        for graph in graphs:
            graph.setGraph()
            rectanglesList = graph.getRectangles()
            smallersList.append(self.getSmallerArea(rectanglesList))
            graph.closeGraph()

        maxArea = max(smallersList)
        smaller = smallersList.index(maxArea)

        if(smaller == 0):
            print("The best option is Pre Order, because its big-smaller area is: ", maxArea)
            return "pre"
        elif(smaller == 1):
            print("The best option is In Order, because its big-smaller area is: ", maxArea)
            return "in"
        else:
            print("The best option is Post Order, because its big-smaller area is: ", maxArea)
            return "post"

root = tk.Tk()
app = Application(master=root)
app.mainloop()
