import math
import time

import numpy as np

import Tree
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class TreeViewer:
    def __init__(self, tree: Tree, window_height: int, window_width: int):
        self.screenH = window_height
        self.screenW = window_width
        self.tree = tree

        self.CountofPics = 360
        self.radius = 0.1

        self.Treelist = [[] for i in range(3)]
        for item in self.tree.get_elements(0):
            self.Treelist[item[0]].append(item[1])

    def clearScreen(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

        gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

    def plotCircle(self, nodeX, nodeY):
        glColor3f(255.0, 255.0, 255.0)
        glPointSize(1.0)
        glBegin(GL_POINTS)

        for i in range(self.CountofPics):
            glVertex2f(round((1 - (nodeX / (self.screenW / 2))) + (self.radius * math.cos(i)), 3),
                       round((0.7 - (nodeY / (self.screenH / 2))) + (self.radius * math.sin(i)), 3))
        glEnd()
        glFlush()



    def plotLine(self, x1: float, y1: float, x2: float, y2: float):
        glBegin(GL_LINES)
        glColor3f(255.0, 255.0, 255.0)
        glVertex2f(round((1 - (x1 / (self.screenW / 2))), 3), round((0.7 - (y1 / (self.screenH / 2))), 3))
        glVertex2f(round((1 - (x2 / (self.screenW / 2))), 3), round((0.7 - (y2 / (self.screenH / 2))), 3))
        glEnd()
        glFlush()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)

        self.XPlotLine = []
        G = []
        self.YPlotLine = []
        for idk, i in enumerate(self.Treelist):
            nodeY = idk * 1000 * self.radius
            self.YPlotLine.append(nodeY)
            step = round(self.screenW / len(i), 2)
            halfstep = 0.5 * step
            for idn, data in enumerate(i):
                nodeX = step * idn + halfstep
                G.append(nodeX)
                self.plotCircle(nodeX, nodeY)
                data.x = nodeX
                data.y = nodeY
            self.XPlotLine.append(G)
            G = []
        for cords in self.tree.getLines():
            self.plotLine(*cords)
        glFlush()

        # glBegin(GL_LINES)
        # # for idk, i in enumerate(self.XPlotLine):
        # for elem,next_elem in zip(self.YPlotLine, self.YPlotLine[1:]+[self.YPlotLine[0]]):
        #     l=0
        #     while l<len(self.XPlotLine[self.YPlotLine.index(next_elem)]):
        #         print(l)
        #         l+=1




            # l=0
            # while l<len(self.XPlotLine[self.YPlotLine.index(next_elem)]):
            #     for i in range(len(self.XPlotLine[l]) - 1):
            #         x1 = round((1 - (self.XPlotLine[self.YPlotLine.index(elem)][l-1] / (int(self.screenW) / 2))), 2)
            #         y1 = round((1 - (elem / (int(self.screenW) / 2))), 2)
            #         print(x1, y1)
            #         print(self.XPlotLine[l][i], elem)
            #         # for i in self.XPlotLine[int(self.YPlotLine.index(elem))]:
            #         #     l+=1

            # for n in elem:
            #     glVertex2f(round((1 - (n / (int(self.screenW) / 2))), 2),
            #                round((0.7 - (int(self.YPlotLine[idk]) / (self.screenH / 2))), 2))
            #     print(round((1 - (n / (self.screenW / 2))), 3),
            #                round((0.7 - (self.YPlotLine[idk] / (self.screenH / 2))), 3))



        glFlush()




    def show(self):
        glutInit()

        glutInitDisplayMode(GLUT_RGB)

        glutCreateWindow("Point")

        glutInitWindowSize(self.screenW, self.screenH)

        glutInitWindowPosition(10, 10)
        print(self.Treelist)
        glutDisplayFunc(self.display)

        self.clearScreen()

        glutMainLoop()
