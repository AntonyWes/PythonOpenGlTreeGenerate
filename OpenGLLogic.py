import math
import dataclasses


import Tree
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class TreeViewer:
    def __init__(self, tree: Tree, window_height: int, window_width: int, treeList: list):
        self.wh = window_height
        self.wd = window_width
        self.shift = 10
        self.tree_w = self.wd - self.shift
        self.tree_h = self.wh - self.shift
        self.tree = tree
        self.Treelist = treeList

        self.CountofPics = 360

    def clearScreen(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

        gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

    def plotCircle(self, R:float):
        glBegin(GL_POINTS)
        for i in range(self.CountofPics):
            glVertex2f(R * math.cos(i), R * math.sin(i))

        glEnd()

    def plotLine(self, x1: int, y1: int, x2: int, y2: int):
        glBegin(GL_LINES)
        glColor3f(0.0, 0.0, 0.0)
        glVertex2i(x1, y1)
        glVertex2i(x2, y2)
        glEnd()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(255.0, 255.0, 255.0)

        glPointSize(1.0)

        for id, i in enumerate(self.Treelist):
            nodeY = id*4*R
            step = self.wd / len(i)
            half-step = 0.5*step
            for idn, data in enumerate(i):
                    nodeX = step * idn + half-step



        self.plotCircle(R)

        glFlush()

    def show(self):
        glutInit()

        glutInitDisplayMode(GLUT_RGB)

        glutCreateWindow("Point")

        glutInitWindowSize(self.wh, self.wd)

        glutInitWindowPosition(self.wh, self.wd)

        glutDisplayFunc(self.display)

        self.clearScreen()

        glutMainLoop()
