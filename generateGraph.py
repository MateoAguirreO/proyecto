# -*- coding: utf-8 -*-
"""
@author: Parjua
"""


import matplotlib.pyplot as plt
import Data


class Graph:
    """
    Class in charge to create the divisions in the plot, get lines and points and save it.
    """
    def __init__(self, tree, type):
        self.tree = tree
        self.maxValue = 25
        self.intersections = []

        if(type == "pre"):
            self.nodes = tree.preOrder()
        elif(type == "in"):
            self.nodes = tree.inOrder()
        elif(type == "post"):
            self.nodes = tree.postOrder()
        else:
            self.nodes = tree.width()

        # Plot Canvas Configurations
        plt.axis([-0.5, self.maxValue+0.5, -0.5, self.maxValue+0.5])  # plt.axis([xmin, xmax, ymin, ymax])
        # plt.legend(loc="upper left")

    def setGraph(self):
        self.setPoints()
        self.drawStraigths()
        # plt.show()

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

    def getIntersections(self):
        return self.intersections

    def getListStraights(self):
        """
        Returns a list of the straights
        """

        straightsList = []
        self.intersections = []

        straightsList.append(self.getStraight("x", 0, 0, 25))
        straightsList.append(self.getStraight("x", 25, 0, 25))
        straightsList.append(self.getStraight("y", 0, 0, 25))
        straightsList.append(self.getStraight("y", 25, 0, 25))

        self.intersections.append([0, 0])
        self.intersections.append([0, 25])
        self.intersections.append([25, 0])
        self.intersections.append([25, 25])

        for node in self.nodes:
            if(self.tree.getNodeLevel(node) % 2 == 0):
                limSouth, limNorth = self.limitVertical(straightsList, node.getValueX(), node.getValueY())
                line = self.getStraight("x", node.getValueX(), limSouth, limNorth)
                self.intersections.append([node.getValueX(), limSouth])
                self.intersections.append([node.getValueX(), limNorth])
                straightsList.append(line)
            else:
                limWest, limEast = self.limitHorizontal(straightsList, node.getValueX(), node.getValueY())
                line = self.getStraight("y", node.getValueY(), limWest, limEast)
                self.intersections.append([limWest, node.getValueY()])
                self.intersections.append([limEast, node.getValueY()])
                straightsList.append(line)

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
        limWest = 0
        limEast = self.maxValue
        linesVertical = []
        linesVerticalValueX = []

        if(not straightsList):
            return limWest, limEast

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

        limWest = self.getProximValue("<", valueX, linesVerticalValueX)
        limEast = self.getProximValue(">", valueX, linesVerticalValueX)

        return limWest, limEast

    def getRectangles(self):
        lines = self.getListStraights()
        intersections = self.getIntersections()
        rectangles = []

        for point in intersections:
            pointX, pointY = point

            if(pointX < self.maxValue and pointY > 0):
                nothing, nextPointX = self.limitHorizontal(lines, pointX, pointY)
                hLine, nothing2 = self.limitVertical(lines, pointX+0.01, pointY)

                if([nextPointX, hLine] in intersections):
                    rectangles.append([point, [nextPointX, hLine]])

        return rectangles

# tree = Data.Data()
# graph = Graph(tree)
# graph.setGraph()
#
# print(graph.getListStraights())
