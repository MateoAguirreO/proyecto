# Importamos los modulos necesarios
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np



class Model3d:


    def __init__(self, regtangles):

        self.xComponents=[]
        self.yComponents=[]
        self.zComponents=[]
        for rectangle in regtangles:
            x1, y1 = rectangle[0]
            x2, y2 = rectangle[1]
            for i in range(y1-y2):
                self.xComponents.append(x1)
                self.yComponents.append(i+y2)
                self.xComponents.append(x2)
                self.yComponents.append(i+y2)
            for j in range(x2-x1):
                self.yComponents.append(y1)
                self.xComponents.append(j+x1)
                self.yComponents.append(y2)
                self.xComponents.append(j+x1)

        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(111, projection='3d')

        # Definimos los datos


        self.zComponents= np.zeros(len(self.xComponents))

        self.dx = np.ones(len(self.xComponents))
        self.dy = np.ones(len(self.xComponents))
        self.dz=[]

        for i in range(len(self.xComponents)):
            self.dz.append(3)

        # utilizamos el método bar3d para graficar las barras
        self.ax1.bar3d(self.xComponents, self.yComponents,self.zComponents , self.dx, self.dy, self.dz)

        # Mostramos el gráfico
        plt.show()








            #print(x1,"-",x2,"--",y1,"-",y2)
