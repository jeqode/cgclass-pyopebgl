from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
import math, sys

WIN_WIDTH, WIN_HEIGHT = 400, 400

tcx, tcy = 0.5, 0.5
tri = [[tcx - 0.5, tcy + 0.5, 1], [tcx - 0.5, tcy - 0.5, 1], [tcx + 0.5, tcy - 0.5, 1]]
mtx = np.matrix(tri)
trans, final_mtx = None, None
transform = False

def init():
	glutInit(sys.argv)
	glutInitWindowSize(WIN_WIDTH,WIN_HEIGHT)
	glutInitWindowPosition(900, 50)
	glutCreateWindow("CG: Homework #01-1 : Triangle Rotate Translate Scale")
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-4, 4, -4, 4)
	glLineWidth(1)
	glClearColor(0.188,0.3137,0.361,1)

def drawAxislines():
	glPushMatrix()
	glColor3ub(0x55,0x62,0x70)
	glBegin(GL_LINES)
	glVertex2f(-10,0)
	glVertex2f(10,0)
	glVertex2f(0,10)
	glVertex2f(0,-10)
	glEnd()
	glPopMatrix()

def drawTriangle():
	global final_mtx, trans
	final_mtx = mtx * trans
	glPushMatrix()
	glColor3ub(0xdf,0x49,0x49)
	glBegin(GL_TRIANGLES)
	for i in range(len(final_mtx)):
		glVertex2f(final_mtx[i, 0], final_mtx[i, 1])
	glEnd()
	glPopMatrix()
	
def transaction():
	global trans
	trans = np.matrix(np.eye(3))

def translate(tx, ty):
	global trans
	t = np.matrix(np.eye(3))
	t[2, 0], t[2, 1] = tx, ty
	trans = trans * t

def rotate(deg):
	global trans
	rad = deg * math.pi / 180
	r = np.matrix(np.eye(3))
	r[0,0] = math.cos(rad)
	r[0,1] = math.sin(rad)
	r[1,0] = -math.sin(rad)
	r[1,1] = math.cos(rad)
	trans = trans * r

def scale(sx, sy):
	global trans
	s = np.matrix(np.eye(3))
	s[0, 0] = sx
	s[1, 1] = sy
	trans = trans * s

def test():
	glColor3ub(0x35,0x79,0x50)
	glPushMatrix()
	glBegin(GL_TRIANGLES)
	glVertex2f(0,1)
	glVertex2f(0,0)
	glVertex2f(1,0)
	glEnd()
	glPopMatrix()
	glPushMatrix()
	glBegin(GL_TRIANGLES)
	glVertex2f(1,1)
	glVertex2f(2,2)
	glVertex2f(3,1)
	glEnd()
	glPopMatrix()

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
	drawAxislines()
	test()
	transaction()
	if (transform):
		translate(-tcx, -tcy)
		rotate(-135) #225
		scale(1.42, 1.42)
		translate(2, 1)
	drawTriangle()
	glutSwapBuffers()

def kb(key, x, y):
	global transform
	if key == b'\x1b':
		sys.exit()
	elif key == b' ':
		transform = not transform
	glutPostRedisplay()

def main():
	print("Press SPACE to transform")
	init()
	glutDisplayFunc(display)
	glutKeyboardFunc(kb)
	glutMainLoop()

if __name__ == "__main__":
	main()