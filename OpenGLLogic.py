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

        for i in self.tree.get_elements(0):
            if int(self.wh) == int(self.tree_w):
                R = (self.wh - (2 * self.shift)) / (2 * self.tree_w)
                nodeX = self.wd / 2
                nodeY = self.wh / 2
            else:
                R = (self.wd - (2 * self.shift)) / (2 * self.tree_w)

                k_x = self.wd - (2 * (self.shift - R)) / (self.tree_w - 1)
                k_y = self.wh - (2 * (self.shift - R)) / (self.tree_h - 1)
                nodeX = k_x * self.Treelist.index(i) + self.shift + R
                for id, data in enumerate(self.Treelist[i]):
                    nodeY = self.wh - k_y * id + self.shift + R



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
