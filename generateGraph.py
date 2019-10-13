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

    with open(filePath, "r") as db:
        dbString = db.read()

    parsedData = json.loads(dbString)

    return parsedData["data"]


def setPoints(points):
    """
    Set the points in the main plot.
    """

    for point in points:
        plt.plot(point["x"], point["y"], "bo", label=point["label"])


def setStraights(points):
    """
    Set the straights int the main plot.
    """

    axis = ["x", "y", "y", "x", "x", "y"]  # This line should contain the ids getted from the tree of Data.py
    i = 0

    for point in points:
        x, y = getStraight(axis[i], point[axis[i]], 0, 21)
        plt.plot(x, y, "red")
        i += 1

# x, y = getStraight("x", 5, 0, 20)
# plt.plot(x, y, "red")

# x, y = getStraight("y", 13, 0, 5)
# plt.plot(x, y, "red")

# x, y = getStraight("y", 15, 5, 20)
# plt.plot(x, y, "red")

# x, y = getStraight("x", 20, 0, 15)
# plt.plot(x, y, "red")

# x, y = getStraight("x", 11, 0, 15)
# plt.plot(x, y, "red")

# x, y = getStraight("y", 8, 11, 20)
# plt.plot(x, y, "red")


filePath = "data.json"
points = getListPoints(filePath)

setPoints(points)
setStraights(points)  # This should be modified

# plt.axis([xmin, xmax, ymin, ymax])
plt.axis([-0.5, 22.5, -0.5, 22.5])

# plt.legend(loc="upper left")

plt.show()
