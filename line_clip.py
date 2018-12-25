from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys, copy

LEFT = 1
RIGHT = 2
TOP = 4
BOTTOM = 8
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

class Line(object):
    def __init__(self, s, p):
        self.point1 = copy.copy(s)
        self.point2 = copy.copy(p)
    @classmethod
    def xy(cls, x1, y1, x2, y2):
        return cls(Point(x1, y1), Point(x2, y2))

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

def drawLine(line):
    glPushMatrix()
    glBegin(GL_LINES)
    glColor3ub(0xdf,0x49,0x49)
    glVertex2f(line.point1.x, line.point1.y)
    glVertex2f(line.point2.x, line.point2.y)
    glEnd()
    glPopMatrix()

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
    if draw: drawLine(line)
    drawWindow(window)
    glutSwapBuffers()

def kbfunc(key, x, y):
    direction = {100:"LEFT", 101:"UP", 102:"RIGHT", 103:"DOWN"}
    if key in direction:
        window.move(direction[key])
    elif key == "\r":
        clipLine()
    glutPostRedisplay()

def encode():
    code = [0, 0]
    for i, point in {0:line.point1, 1:line.point2}.items():
        for side in [LEFT, RIGHT, TOP, BOTTOM]:
            if point.isOutOf_On_Side(window, side):
                code[i] = code[i] | side
    return code

def clipLine():
    while True:
        global draw
        code1, code2 = encode()
        if not code1 | code2:
            draw = True
            break
        elif code1 & code2:
            draw = False
            break
        else:
            p1 = line.point1
            p2 = line.point2
            if not code1:
                p1, p2, code1, code2 = p2, p1, code2, code1
            dx = p2.x - p1.x
            dy = p2.y - p1.y
            m = dy / dx
            b = p2.y - m * p2.x
            if code1 & LEFT:
                p1.x = window.minPoint.x
                p1.y = m * p1.x + b
            elif code1 & RIGHT:
                p1.x = window.maxPoint.x
                p1.y = m * p1.x + b
            elif code1 & TOP:
                p1.y = window.maxPoint.y
                p1.x = (p1.y - b) / m
            elif code1 & BOTTOM:
                p1.y = window.minPoint.y
                p1.x = (p1.y - b) / m

"""main"""
draw = True
window = Window.xy(-0.2, -0.2, 0.2, 0.2)
line = Line(Point(-1, -1), Point(1,1))
initial()
glutKeyboardFunc(kbfunc)
glutSpecialFunc(kbfunc)
glutDisplayFunc(display)
glutMainLoop()