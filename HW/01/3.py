from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

WIN_WIDTH, WIN_HEIGHT = 400, 400

def init():
	glutInit(sys.argv)
	glutInitWindowSize(WIN_WIDTH,WIN_HEIGHT)
	glutInitWindowPosition(900, 50)
	glutCreateWindow("CG: Homework #01-3 : Trace Program")
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-6, 6, -6, 6)
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

def drawShape():
	glBegin(GL_POLYGON)
	glVertex2f(0, 0)
	glVertex2f(2, 0)
	glVertex2f(2, 1)
	glVertex2f(1, 1)
	glVertex2f(1, 3)
	glVertex2f(0, 3)
	glEnd()

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
	drawAxislines()

	glColor3ub(0xdf,0x49,0x49)
	drawShape() #shape 1 : Red
	
	glRotate(90, 0, 0, 1)
	glTranslate(1, 0, 0)
	glColor3ub(0xaa,0xaa,0xaa)
	drawShape() #shape 2 : White

	glRotate(-90, 0, 0, 1)
	glPushMatrix()

	glTranslate(1, 0, 0)
	glColor3ub(0xc0,0x49,0xa9)
	drawShape() #shape 3 : Magenta

	glScale(1, 2, 1)
	glTranslate(1, -2, 0)
	glColor3ub(0x20,0xa9,0x49)
	drawShape() #shape 4 : Green

	glTranslate(-2, 2, 0)
	glRotate(90, 0, 0, 1)
	glTranslate(-1, -1, 0)
	glScale(1, .5, 1)
	glRotate(90, 0, 0, 1)

	glPopMatrix()

	glTranslate(-2, 1, 0)
	glColor3ub(0x40,0x49,0xa9)
	drawShape() #shape 5 : Blue

	glutSwapBuffers()

def main():
	init()
	glutDisplayFunc(display)
	glutMainLoop()

if __name__ == "__main__":
	main()