# -*- coding: utf-8 -*-
"""
@author: Parjua
"""


import tkinter as tk
from PIL import Image, ImageTk
import generateGraph
import Data


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("850x600")
        self.pack()
        self.createWidgets()
        self.canvas = None

        self.tree = Data.Data()
        self.graph = generateGraph.Graph(self.tree)

    def createWidgets(self):
        self.i = 0

        self.btnNextGraph = tk.Button(self)
        self.btnNextGraph["text"] = "> Next"
        self.btnNextGraph["command"] = self.nextGraph
        self.btnNextGraph.pack(side="top")

        self.btnResetGraph = tk.Button(self)
        self.btnResetGraph["text"] = "Delete Graph"
        self.btnResetGraph["command"] = self.deleteGraph
        self.btnResetGraph.pack(side="top")

        self.btnQuit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.btnQuit.pack(side="bottom")

    def createCanvas(self):
        self.canvas = tk.Canvas(self.master, width=850, height=400)
        self.canvas.pack()

    def nextGraph(self):
        if(self.canvas):
            if(self.i == len(self.tree.preOrd())):
                self.i = 0
            img1 = Image.open("img/"+str(self.i)+".png")
            self.image1 = ImageTk.PhotoImage(img1.resize((512, 384)))
            self.canvas.create_image(420, 200, image=self.image1)
            self.i += 1
        else:
            self.createCanvas()
            self.nextGraph()

    def deleteGraph(self):
        if(self.canvas):
            self.canvas.destroy()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
