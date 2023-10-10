import math
import dataclasses


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
        self.radius = 1

        self.Treelist = [[] for i in range(3)]
        for item in self.tree.get_elements(0):
            self.Treelist[item[0]].append(item[1])

    def clearScreen(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)

        gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

    def plotCircle(self, nodeX, nodeY):
        glBegin(GL_POINTS)

        twicePi = 2*math.pi
        for i in range(self.CountofPics):
            glVertex2f(nodeX, nodeY)
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

        glPointSize(10.0)

        for id, i in enumerate(self.Treelist):
            nodeY = id*4*self.radius
            step = self.screenW / len(i)
            halfstep = 0.5*step
            for idn, data in enumerate(i):
                    nodeX = step * idn + halfstep



        self.plotCircle(nodeX, nodeY)

        glFlush()

    def show(self):
        glutInit(sys.argv)

        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)

        glutCreateWindow("Point")

        glutInitWindowSize(GL_INT, GL_INT)

        glutInitWindowPosition(10, 10)

        print(glutGet(GLUT_WINDOW_WIDTH))
        print(glutGet(GLUT_WINDOW_HEIGHT))

        glutDisplayFunc(self.display)

        self.clearScreen()

        glutMainLoop()
