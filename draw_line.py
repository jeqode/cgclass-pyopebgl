from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, copy

WIN_WIDTH = 400
WIN_HEIGHT = WIN_WIDTH
STEP = 2.0 / WIN_WIDTH

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getCoordinate(self):
        return x, y

def initial ():
    glutInit(sys.argv)
    glutInitWindowSize(WIN_WIDTH,WIN_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Draw line function")
    glLineWidth(1)
    glClearColor(0.188,0.3137,0.361,1)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glPushMatrix()
    glColor3ub(0x55,0x62,0x70)
    glBegin(GL_LINES)
    glVertex2f(-1,0)
    glVertex2f(1,0)
    glVertex2f(0,1)
    glVertex2f(0,-1)
    glEnd()
    glPopMatrix()
    glColor3ub(0xdf,0x49,0x49)
    drawLine(p1, p2)
    glutSwapBuffers()

def drawLine(p1, p2):
    glPushMatrix()
    glBegin(GL_POINTS)
    if p1.x > p2.x: p1, p2 = p2, p1
    dy = p2.y - p1.y
    dx = p2.x - p1.x
    if dx == 0:
        if p1.y > p2.y: p1, p2 = p2, p1
        y = p1.y
        while y <= p2.y:
            glVertex2f(p1.x, y)
            y += STEP
    else:
        m = dy / dx
        b = p2.y - m * p2.x
        x = p1.x
        while x <= p2.x:
            y = x * m + b
            glVertex2f(x, y)
            x += STEP
    glEnd()
    glPopMatrix

"""main"""
initial()
p1 = Point(-0.25, -0.25)
p2 = Point(0.3, 0.32)
glutDisplayFunc(display)
glutMainLoop()