from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
TITLE = "CG: Homework #02-05 : Projection"
WIDTH, HEIGHT = 500, 500
view, en_light, en_blend = True, True, True
eye_x, eye_y, eye_z = 0, 0, 10
center_x, center_y, center_z = 0, 0, -10
theta = 0

light = {
	"pos": [10, 10, 10, 0],
	"dif": [1.0, 1.0, 1.0, 1.0],
	"amb": [0.8, 0.8, 0.8, 1.0],
	"spc": [1.0, 1.0, 1.0, 1.0]
}

mat = [
	{
		"dif": [1.0, 1.0, 0.0, 0.7],
		"amb": [0.8, 0.8, 0.0, 0.7],
		"spc": [1.0, 1.0, 0.8, 0.7],
		"shn": 10
	},{
		"dif": [1.0, 0.0, 0.0, 0.7],
		"amb": [0.8, 0.0, 0.0, 0.7],
		"spc": [1.0, 0.6, 0.6, 0.7],
	},{
		"dif": [0.0, 1.0, 0.0, 0.7],
		"amb": [0.0, 0.8, 0.0, 0.7],
		"spc": [0.6, 1.0, 0.6, 0.7],
	}
]

def init():
	glutInit()
	glutInitWindowSize(WIDTH, HEIGHT)
	glutInitWindowPosition(800, 5)
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
	glutCreateWindow(TITLE)
	glClearColor(0.1, 0.1, 0.1, 1.0)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, light["dif"])
	glLightfv(GL_LIGHT0, GL_AMBIENT, light["amb"])
	glLightfv(GL_LIGHT0, GL_SPECULAR, light["spc"])
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def kb(key, x, y):
	global view, en_light, eye_x, eye_y, eye_z, en_blend
	if key == b'\x1b':
		sys.exit()
	elif key == b'v':
		view = not view
	elif key == b'l':
		en_light = not en_light
	elif key == b',':
		eye_x -= 1
	elif key == b'.':
		eye_x += 1
	elif key == b'b':
		en_blend = not en_blend
	elif key == 100:
		eye_x -= 1
	elif key == 102:
		eye_x += 1
	elif key == 101:
		eye_z -= 1
	elif key == 103:
		eye_z += 1

	glutPostRedisplay()

def idle():
	global theta
	if theta == 360: 
		theta = 1
	else:
		theta += 1
	glutPostRedisplay()

def setScene():
	glViewport(0, 0, WIDTH, HEIGHT)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	if view:
		gluPerspective(90., 1., 1, 35)
	else:
		glOrtho(-10, 10, -10, 10, 1, 35)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(eye_x, eye_y, eye_z, eye_x, eye_y, center_z, 0, 1, 0)
	if en_light:
		glEnable(GL_LIGHTING)
	else:
		glDisable(GL_LIGHTING)
	if en_blend:
		glEnable(GL_BLEND)
	else:
		glDisable(GL_BLEND)
	glPushMatrix()
	glRotatef(theta, 0, 1, 0)
	glLightfv(GL_LIGHT0, GL_POSITION, light["pos"])
	glPopMatrix()
	
def display():
	setScene()
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPushMatrix()
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[2]["dif"])
	glMaterialfv(GL_FRONT, GL_AMBIENT, mat[2]["amb"])
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat[2]["spc"])
	glTranslatef(20, 0, -2)
	glColor4fv(mat[2]["dif"])
	glutSolidSphere(2, 80, 80)
	glPopMatrix()
	glPushMatrix()
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[1]["dif"])
	glMaterialfv(GL_FRONT, GL_AMBIENT, mat[1]["amb"])
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat[1]["spc"])
	glTranslatef(-3, 0, -2)
	glColor4fv(mat[1]["dif"])
	glutSolidSphere(2, 80, 80)
	glPopMatrix()
	glPushMatrix()
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[0]["dif"])
	glMaterialfv(GL_FRONT, GL_AMBIENT, mat[0]["amb"])
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat[0]["spc"])
	glMaterialfv(GL_FRONT, GL_SHININESS, mat[0]["shn"])
	glColor4fv(mat[0]["dif"])
	glutSolidSphere(2, 80, 80)
	glPopMatrix()
	glutSwapBuffers()

def main():
	init()
	glutDisplayFunc(display)
	glutKeyboardFunc(kb)
	glutSpecialFunc(kb)
	glutIdleFunc(idle)
	glutMainLoop()

if __name__ == "__main__":
	main()
	