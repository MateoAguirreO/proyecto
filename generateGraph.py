import matplotlib.pyplot as plt


def getRecta(eje, value, end, start=0):
    axeX, axeY = [], []
    eje = eje.lower()
    
    if(eje == "x"):
        for i in range(start, end + 1):
            axeX.append(value)
            axeY.append(i)
    else:
        for i in range(start, end + 1):
            axeX.append(i)
            axeY.append(value)
    
    return axeX, axeY


puntos = [[5, 8], [1, 13], [10, 15], [11, 15], [20, 12], [14, 8]]

for par in puntos:
    plt.plot(par[0], par[1], "ro")

x, y = getRecta("x", 5, 20)
plt.plot(x, y, "red")

x, y = getRecta("y", 13, 5)
plt.plot(x, y, "red")

x, y = getRecta("y", 15, 20, 5)
plt.plot(x, y, "red")

x, y = getRecta("x", 20, 15)
plt.plot(x, y, "red")

x, y = getRecta("x", 11, 15)
plt.plot(x, y, "red")

x, y = getRecta("y", 8, 20, 11)
plt.plot(x, y, "red")

# plt.axis([xmin, xmax, ymin, ymax])
plt.axis([-0.5, 20.5, -0.5, 20.5])

plt.show()
