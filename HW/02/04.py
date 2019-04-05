from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
TITLE = b'CG: Homework #02-04 : Lighting'
WIDTH, HEIGHT = 500, 500
theta, view = 0, 0
en_light = True
shn = 4

light = {
	"pos": [4, 8, 10, 0],
	"dif": [1.0, 1.0, 1.0, 1.0],
	"amb": [0.8, 0.8, 0.8, 1.0],
	"spc": [1.0, 1.0, 1.0, 1.0]
}

mat = {
	"dif": [0.0, 0.0, 0.6, 1],
	"amb": [0.0, 0.0, 0.4, 1],
	"spc": [1.0, 0.0, 1.0, 1],
	"shn": shn
}

def init():
	glutInit()
	glutInitWindowSize(WIDTH, HEIGHT)
	glutInitWindowPosition(800, 50)
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
	glutCreateWindow(TITLE)
	glClearColor(0.1, 0.1, 0.1, 1.0)
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, light["dif"])
	glLightfv(GL_LIGHT0, GL_AMBIENT, light["amb"])
	glLightfv(GL_LIGHT0, GL_SPECULAR, light["spc"])

def idle():
	global theta
	if theta == 360: 
		theta = 1
	else:
		theta += 1
	glutPostRedisplay()

def kb(key, x, y):
	global view, en_light, shn
	if key == b'\x1b':
		sys.exit()
	elif key == b'v':
		if view == 2:
			view = 0
		else:
			view += 1
	elif key == b'l':
		en_light = not en_light
	elif key == b's':
		shn += 1
		print("Shininess : %d" % shn)
	elif key == b'a':
		shn -= 1
		print("Shininess : %d" % (shn))
	glutPostRedisplay()

def setScene():
	glViewport(0, 0, WIDTH, HEIGHT)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	if view == 0:
		gluPerspective(90., 1., 0.5, 80.)
	elif view == 1:
		glFrustum(-5, 5, -5, 5, 5, 80)
	else:
		glOrtho(-31, 31, -31, 31, 0, 80)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(0, 10, 30, 0, 0, -1, 0, 1, 0)
	if en_light:
		glEnable(GL_LIGHTING)
	else:
		glDisable(GL_LIGHTING)

def display():
	setScene()
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPushMatrix()
	glRotatef(theta, 0, 1, 0)
	
	glPushMatrix()
	glDisable(GL_LIGHTING)
	glTranslatef(light["pos"][0], light["pos"][1], light["pos"][2])
	glutSolidCube(1)
	glEnable(GL_LIGHTING)
	glPopMatrix()

	glLightfv(GL_LIGHT0, GL_POSITION, light["pos"])
	glPopMatrix()

	glPushMatrix()
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat["dif"])
	glMaterialfv(GL_FRONT, GL_AMBIENT, mat["amb"])
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat["spc"])
	glMaterialfv(GL_FRONT, GL_SHININESS, shn)
	glColor3ub(0, 0, 100)
	glutSolidSphere(10, 80, 80)
	glPopMatrix()
	glutSwapBuffers()

def main():
	init()
	glutDisplayFunc(display)
	glutKeyboardFunc(kb)
	glutIdleFunc(idle)
	glutMainLoop()

if __name__ == "__main__":
	main()