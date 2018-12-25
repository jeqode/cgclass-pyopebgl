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
    def isIn(self, w):
        return w.minPoint.x <= self.x <= w.maxPoint.x and w.minPoint.y <= self.y <= w.maxPoint.y
    def isOutOf_On_Side(self, w, side):
        if side == LEFT:
            return self.x < w.minPoint.x
        elif side == RIGHT:
            return self.x > w.maxPoint.x
        elif side == TOP:
            return self.y > w.maxPoint.y
        elif side == BOTTOM:
            return self.y < w.minPoint.y
    def __str__(self):
        return "Point(%s, %s)" % (self.x, self.y)

class Window(object):
    def __init__(self, minPoint, maxPoint):
        self.minPoint = copy.copy(minPoint)
        self.maxPoint = copy.copy(maxPoint)
    @classmethod
    def xy(cls, minX, minY, maxX, maxY):
        return cls(Point(minX, minY), Point(maxX, maxY))
    def move(self, direction):
        sign = 1
        if direction == "LEFT" or direction == "DOWN":
            sign = -1
        if direction == "LEFT" or direction == "RIGHT":
            self.minPoint.x += sign * STEP
            self.maxPoint.x += sign * STEP
        else:
            self.minPoint.y += sign * STEP
            self.maxPoint.y += sign * STEP

def initial ():
    glutInit(sys.argv)
    glutInitWindowSize(WIN_WIDTH,WIN_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Line Clip")
    glLineWidth(1)
    glClearColor(0.188,0.3137,0.361,1)

def drawWindow(w):
    glPushMatrix()
    glColor3ub(0xef,0xc9,0x4c)
    glBegin(GL_POLYGON)
    glVertex2f(w.minPoint.x, w.maxPoint.y)
    glVertex2f(w.maxPoint.x, w.maxPoint.y)
    glVertex2f(w.maxPoint.x, w.minPoint.y)
    glVertex2f(w.minPoint.x, w.minPoint.y)
    glEnd()
    glPopMatrix()

def kbfunc(key, x, y):
    direction = {100:"LEFT", 101:"UP", 102:"RIGHT", 103:"DOWN"}
    if key in direction:
        window.move(direction[key])
    elif key == "\r":
        pass
    glutPostRedisplay()

def drawPolygon(points):
    glPushMatrix()
    glBegin(GL_POLYGON)
    glColor3ub(0xdf,0x49,0x49)
    for p in points:
        glVertex2f(p.x, p.y)
    glEnd()
    glPopMatrix()

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
    if draw: drawPolygon(points)
    drawWindow(window)
    glutSwapBuffers()

def clipPolygon(points):
    pass

"""main"""
draw = True
window = Window.xy(-0.2, -0.2, 0.2, 0.2)
points = []
points.append(Point(-0.35, 0.35))
points.append(Point(0.15, 0.15))
points.append(Point(0.25, 0.19))
points.append(Point(0.25, -0.32))
points.append(Point(0.12, -0.15))
points.append(Point(-0.18, -0.18))
initial()
glutKeyboardFunc(kbfunc)
glutSpecialFunc(kbfunc)
glutDisplayFunc(display)
glutMainLoop()