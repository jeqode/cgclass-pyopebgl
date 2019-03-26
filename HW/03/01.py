from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
TITLE = "CG: Homework #03-01 : Lighting positioning"
WIDTH, HEIGHT = 500, 500
view = 0
eye_x, eye_y = 0, 20
en_light = True

light = {
	"pos": [10, 5, 10, 1],
	"dif": [1.0, 1.0, 1.0, 1.0],
	"amb": [0.4, 0.4, 0.4, 1.0],
	"spc": [0.8, 0.8, 0.8, 1.0]
}

mat = {
	"dif": [0.0, 1.0, 1.0, 1.0],
	"amb": [0.0, 0.6, 0.6, 1.0],
	"spc": [0.0, 0.8, 0.8, 1.0],
	"shn": 20
}

def init():
	glutInit()
	glutInitWindowSize(WIDTH, HEIGHT)
	glutInitWindowPosition(800, 50)
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
	glutCreateWindow(TITLE)
	glClearColor(0.1, 0.1, 0.1, 1.0)
	glShadeModel(GL_SMOOTH)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, light["dif"])
	glLightfv(GL_LIGHT0, GL_AMBIENT, light["amb"])
	glLightfv(GL_LIGHT0, GL_SPECULAR, light["spc"])

def kb(key, x, y):
	global view, en_light, eye_x, eye_y
	if key == b'\x1b':
		sys.exit()
	elif key == b'v':
		if view == 2:
			view = 0
			print("Perspective")
		else:
			view += 1
			print("Frustum" if view == 1 else "Ortho")
	elif key == b'l':
		en_light = not en_light
		print("Light enabled" if en_light else "Light disabled")
	elif key == 100:
		eye_x -= 1
	elif key == 102:
		eye_x += 1
	elif key == 101:
		eye_y += 1
	elif key == 103:
		eye_y -= 1
	glutPostRedisplay()

def setScene():
	glViewport(0, 0, WIDTH, HEIGHT)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	if view == 0:
		gluPerspective(90., 1., 0.5, 80.)
	elif view == 1:
		glFrustum(-12, 12, -12, 12, 5, 80)
	else:
		glOrtho(-22, 22, -22, 22, 5, 80)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(eye_x, eye_y, 20, eye_x, 0, -1, 0, 1, 0)
	if en_light:
		glEnable(GL_LIGHTING)
	else:
		glDisable(GL_LIGHTING)
	glLightfv(GL_LIGHT0, GL_POSITION, light["pos"])

def drawPlane(w, h):
	dw = 1.0 / w
	dh = 1.0 / h
	# glNormal3f(0.0, 0.0, 1.0)
	for j in range(h):
		glBegin(GL_TRIANGLE_STRIP)
		for i in range(w):
			glVertex2f(dw * i, dh * (j + 1))
			glVertex2f(dw * i, dh * j)
			# print("(%f, %f) - (%f, %f)" % (dw * i, dh * (j + 1), dw * i, dh * j))
		glEnd()

def display():
	setScene()
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat["dif"])
	glMaterialfv(GL_FRONT, GL_AMBIENT, mat["amb"])
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat["spc"])
	glMaterialfv(GL_FRONT, GL_SHININESS, mat["shn"])

	glPushMatrix()
	glColor4fv(mat["dif"])
	glRotatef(-90.0, 1, 0, 0)
	glScalef(20, 20, 1)
	glTranslatef(-0.5, -0.5, 0.0)
	drawPlane(20, 20)
	# glBegin(GL_POLYGON)
	# glVertex2f(-0.5, -0.5)
	# glVertex2f(0.5, -0.5)
	# glVertex2f(0.5, 0.5)
	# glVertex2f(-0.5, 0.5)
	# glEnd()
	glPopMatrix()
	glutSwapBuffers()

def main():
	init()
	glutDisplayFunc(display)
	glutKeyboardFunc(kb)
	glutSpecialFunc(kb)
	glutMainLoop()

if __name__ == "__main__":
	main()