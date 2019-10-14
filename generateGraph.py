# -*- coding: utf-8 -*-
"""
@author: Parjua
"""


import matplotlib.pyplot as plt
import json
import Data


class Graph:
    """
    Class in charge to create the divisions in the plot, get lines and points and save it.
    """
    def __init__(self, tree):
        self.tree = tree
        self.nodes = tree.preOrd()
        self.maxValue = 25

        # Plot Canvas Configurations
        plt.axis([-0.5, self.maxValue+0.5, -0.5, self.maxValue+0.5])  # plt.axis([xmin, xmax, ymin, ymax])
        plt.legend(loc="upper left")

    def showPlot(self):
        self.setPoints()
        self.drawStraigths()
        plt.show()

    def getStraight(self, axis, value, start, end):
        """
        Return two lists required to make a straight.
        Params: 1) axis where the value will be.
                2) value in the axis.
                3) point to start on the opposite axis.
                4) point to end on the opposite axis.
        """

        axisX, axisY = [], []
        axis = axis.lower()
        
        if(axis == "x"):
            axisX = [value, value]
            axisY = [start, end]
        else:
            axisX = [start, end]
            axisY = [value, value]
        
        return axisX, axisY

    def setPoints(self):
        """
        Set the points in the main plot.
        """

        for node in self.nodes:
            plt.plot(node.getValueX(), node.getValueY(), "bo")

    def getListStraights(self):
        """
        Returns a list of the straights
        """

        straightsList = []

        for node in self.nodes:
            if(tree.getNodeLevel(node) % 2 == 0):
                limSouth, limNorth = self.limitVertical(straightsList, node.getValueX(), node.getValueY())
                straightsList.append(self.getStraight("x", node.getValueX(), limSouth, limNorth))
            else:
                limSouth, limNorth = self.limitHorizontal(straightsList, node.getValueX(), node.getValueY())
                straightsList.append(self.getStraight("y", node.getValueY(), limSouth, limNorth))

        return straightsList


    def drawStraigths(self):
        """
        Draw the straights on the main plot and save the step-by-step on the folder /img/.
        """

        straightsList = self.getListStraights()
        
        i = 0
        for straight in straightsList:
            plt.plot(straight[0], straight[1])
            # Line to save the png's of each step in the process of making the straights
            plt.savefig("img/"+str(i)+".png")
            i += 1

    def getProximValue(self, side, value, listofValues):
        """
        Return the closer value being, minor or major, of a value between a list of values.
        """

        answer = 0

        if(side.lower() == "<"):
            for item in listofValues:
                if(item < value and item > answer):
                    answer = item
        else:
            answer = self.maxValue
            for item in listofValues:
                if(item > value and item < answer):
                    answer = item

        return answer

    def limitVertical(self, straightsList, valueX, valueY):
        """
        Return one limit in the south and one in the north between a list of starights
        """
        
        limSouth = 0
        limNorth = self.maxValue
        linesHorizontal = []
        linesHorizontalValueY = []

        # If the list passed by param is empty return 0, 25
        if(not straightsList):
            return limSouth, limNorth

        # This bucle get all the horizontal lines in the plot and get its Y value
        for line in straightsList:
            if(line[1][0] == line[1][1]):
                linesHorizontal.append(line)

        # This bucle add to a list the Y value of an horizontal straight if this horizontal
        # straight will cut our vertical straight in some point
        for line in linesHorizontal:
            lineStartX = line[0][0]
            lineEndX = line[0][1]
            lineY = line[1][0]

            if(lineStartX <= valueX and valueX <= lineEndX):
                linesHorizontalValueY.append(lineY)

        limSouth = self.getProximValue("<", valueY, linesHorizontalValueY)
        limNorth = self.getProximValue(">", valueY, linesHorizontalValueY)

        return limSouth, limNorth

    def limitHorizontal(self, straightsList, valueX, valueY):
        limSouth = 0
        limNorth = self.maxValue
        linesVertical = []
        linesVerticalValueX = []

        if(not straightsList):
            return limSouth, limNorth

        # This bucle get all the horizontal lines in the plot and get its Y value
        for line in straightsList:
            if(line[0][0] == line[0][1]):
                linesVertical.append(line)

        for line in linesVertical:
            lineStartY = line[1][0]
            lineEndY = line[1][1]
            lineX = line[0][0]

            if(lineStartY <= valueY and valueY <= lineEndY):
                linesVerticalValueX.append(lineX)

        limSouth = self.getProximValue("<", valueX, linesVerticalValueX)
        limNorth = self.getProximValue(">", valueX, linesVerticalValueX)

        return limSouth, limNorth


tree = Data.Data()
graph = Graph(tree)
graph.showPlot()
