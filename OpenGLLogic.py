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
        glBegin(GL_POLYGON)

        for i in range(self.CountofPics):
            glVertex2f(round((1 - (nodeX / (self.screenW / 2))) + (self.radius * math.cos(i)), 3),
                       round((0.7 - (nodeY / (self.screenH / 2))) + (self.radius * math.sin(i)), 3))
        glEnd()
        glFlush()



    def plotLine(self, x1: int, y1: int, x2: int, y2: int):
        glBegin(GL_LINES)
        glColor3f(255.0, 255.0, 255.0)
        glVertex2i(x1, y1)
        glVertex2i(x2, y2)
        glEnd()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)

        self.XPlotLine = []
        self.YPlotLine = []

        for idk, i in enumerate(self.Treelist):
            nodeY = idk * 1000 * self.radius
            step = self.screenW / len(i)
            halfstep = 0.5 * step
            for idn, data in enumerate(i):
                nodeX = step * idn + halfstep
                self.plotCircle(nodeX, nodeY)
        print("X " + str(self.XPlotLine))
        print("Y " + str(self.YPlotLine))

    def show(self):
        glutInit()

        glutInitDisplayMode(GLUT_RGB)

        glutCreateWindow("Point")

        glutInitWindowSize(self.screenW, self.screenH)

        glutInitWindowPosition(10, 10)

        glutDisplayFunc(self.display)

        self.clearScreen()

        glutMainLoop()
