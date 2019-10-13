# -*- coding: utf-8 -*-
"""
@author: Parjua
"""


import matplotlib.pyplot as plt
import json


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


def getListPoints(filePath):
    """
    Returns a list of dictionaries, that contain points, from a JSON file in 'filePath'.
    """

    db = open(filePath, "r")
    dbString = db.read()
    parsedData = json.loads(dbString)

    return parsedData["data"]


def setPoints(points):
    """
    Set the points in the main plot.
    """

    for point in points:
        plt.plot(point["x"], point["y"], "bo", label=point["label"])


filePath = "data.json"
points = getListPoints(filePath)

setPoints(points)

# plt.axis([xmin, xmax, ymin, ymax])
plt.axis([-0.5, 20.5, -0.5, 20.5])

# plt.legend(loc="upper left")

plt.show()
