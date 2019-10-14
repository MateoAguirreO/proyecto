# -*- coding: utf-8 -*-
"""
@author: Parjua
"""


import matplotlib.pyplot as plt
import json
import Data


def getStraight(axis, value, start, end):
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


def setPoints(points):
    """
    Set the points in the main plot.
    """

    for point in points:
        plt.plot(point["x"], point["y"], "bo")


def setStraights(tree):
    """
    Set the straights on the main plot.
    """

    nodes = tree.preOrd()
    straightsList = []

    for node in nodes:
        if(tree.getNodeLevel(node) % 2 == 0):
            straightsList.append(getStraight("x", node.getValueX(), 0, 21))
        else:
            straightsList.append(getStraight("y", node.getValueY(), 0, 21))
    
    for straight in straightsList:
        plt.plot(straight[0], straight[1])


tree = Data.Data()
points = tree.getListPoints()

setPoints(points)
setStraights(tree)

# Plot Canvas Configurations
plt.axis([-0.5, 22.5, -0.5, 22.5])  # plt.axis([xmin, xmax, ymin, ymax])
plt.legend(loc="upper left")

plt.show()
