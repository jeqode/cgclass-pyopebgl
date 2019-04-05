from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
TITLE = "CG: Homework #02-01 : Lighting positioning"
WIDTH, HEIGHT = 500, 500
lighti, view = 0, 2
en_light = True
red, green, blue = False, False, False
lights = [GL_LIGHT0, GL_LIGHT1, GL_LIGHT2, GL_LIGHT3, GL_LIGHT4, GL_LIGHT5]

light = [
	{#0
		"pos": [0, 0, -20, 0],
		"diff": [1.0, 1.0, 1.0, 1.0],
		"amb": [0.0, 0.0, 0.0, 1.0],
		"spc": [0.0, 0.0, 0.0, 1.0]
	},{#1
		"pos": [0, 0, 20, 0],
		"diff": [1.0, 1.0, 1.0, 1.0],
		"amb": [0.0, 0.0, 0.0, 1.0],
		"spc": [0.0, 0.0, 0.0, 1.0]
	},{#2
		"pos": [0, 20, 0, 0],
		"diff": [1.0, 1.0, 1.0, 1.0],
		"amb": [0.0, 0.0, 0.0, 1.0],
		"spc": [0.0, 0.0, 0.0, 1.0]
	},{#3
		"pos": [30, 0, 0, 0],
		"diff": [1.0, 1.0, 1.0, 1.0],
		"amb": [0.0, 0.0, 0.0, 1.0],
		"spc": [0.0, 0.0, 0.0, 1.0]
	},{#4
		"pos": [30, 30, 0, 0],
		"diff": [1.0, 1.0, 1.0, 1.0],
		"amb": [0.0, 0.0, 0.0, 1.0],
		"spc": [0.0, 0.0, 0.0, 1.0]
	},{#5
		"pos": [30, 30, 30, 0],
		"diff": [1.0, 1.0, 1.0, 1.0],
		"amb": [0.0, 0.0, 0.0, 1.0],
		"spc": [0.0, 0.0, 0.0, 1.0]
	}
]

mat = [
	{
		"dif": [1.0, 1.0, 1.0, 0.5],
		"amb": [0.8, 0.8, 0.8, 0.5],
		"spc": [1.0, 1.0, 1.0, 0.5],
		"shn": 10
	},
	{
		"dif": [1.0, 0.0, 0.0, 0.5],
		"amb": [0.8, 0.0, 0.0, 0.5],
		"spc": [1.0, 0.0, 0.0, 0.5],
		"shn": 10
	},{
		"dif": [0.0, 1.0, 0.0, 0.5],
		"amb": [0.0, 0.8, 0.0, 0.5],
		"spc": [0.0, 1.0, 0.6, 0.5],
		"shn": 10
	},{
		"dif": [0.0, 0.0, 1.0, 0.5],
		"amb": [0.0, 0.0, 0.8, 0.5],
		"spc": [0.0, 0.0, 1.0, 0.5],
		"shn": 10
	}
]

def init():
	glutInit()
	glutInitWindowSize(WIDTH, HEIGHT)
	glutInitWindowPosition(800, 50)
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
	glutCreateWindow(TITLE)
	glClearColor(0.7, 0.7, 0.7, 1.0)
	glShadeModel(GL_SMOOTH)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)
	for i in range(6):
		glLightfv(lights[i], GL_POSITION, light[i]["pos"])
		glLightfv(lights[i], GL_DIFFUSE, light[i]["diff"])
		glLightfv(lights[i], GL_AMBIENT, light[i]["amb"])
		glLightfv(lights[i], GL_SPECULAR, light[i]["spc"])

def kb(key, x, y):
	global view, en_light, lighti, red, green, blue
	glDisable(lights[lighti])
	if key == b'\x1b':
		sys.exit()
	elif key == b'v':
		if view == 2:
			view = 0
		else:
			view += 1
	elif key == b'l':
		en_light = not en_light
	elif key == b'4':
		lighti = 0
	elif key == b'5':
		lighti = 1
	elif key == b'6':
		lighti = 2
	elif key == b'7':
		lighti = 3
	elif key == b'8':
		lighti = 4
	elif key == b'9':
		lighti = 5
	elif key == b'1':
		red = not red
	elif key == b'2':
		green = not green
	elif key == b'3':
		blue = not blue
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
	gluLookAt(0, 0, 32, 0, 0, 0, 0, 1, 0)
	if en_light:
		glEnable(GL_LIGHTING)
	else:
		glDisable(GL_LIGHTING)
	glEnable(lights[lighti])

def display():
	setScene()
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glPushMatrix()
	glTranslatef(-20, 0, 0)
	if red:
		glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[1]["dif"])
		glMaterialfv(GL_FRONT, GL_AMBIENT, mat[1]["amb"])
		glMaterialfv(GL_FRONT, GL_SPECULAR, mat[1]["spc"])
		glMaterialfv(GL_FRONT, GL_SHININESS, mat[1]["shn"])
	else:
		glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[0]["dif"])
		glMaterialfv(GL_FRONT, GL_AMBIENT, mat[0]["amb"])
		glMaterialfv(GL_FRONT, GL_SPECULAR, mat[0]["spc"])
		glMaterialfv(GL_FRONT, GL_SHININESS, mat[0]["shn"])
	glutSolidSphere(8, 80, 80)
	glPopMatrix()
	glPushMatrix()
	if green:
		glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[2]["dif"])
		glMaterialfv(GL_FRONT, GL_AMBIENT, mat[2]["amb"])
		glMaterialfv(GL_FRONT, GL_SPECULAR, mat[2]["spc"])
		glMaterialfv(GL_FRONT, GL_SHININESS, mat[2]["shn"])
	else:
		glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[0]["dif"])
		glMaterialfv(GL_FRONT, GL_AMBIENT, mat[0]["amb"])
		glMaterialfv(GL_FRONT, GL_SPECULAR, mat[0]["spc"])
		glMaterialfv(GL_FRONT, GL_SHININESS, mat[0]["shn"])
	glutSolidSphere(8, 80, 80)
	glPopMatrix()
	glPushMatrix()
	glTranslatef(20, 0, 0)
	if blue:
		glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[3]["dif"])
		glMaterialfv(GL_FRONT, GL_AMBIENT, mat[3]["amb"])
		glMaterialfv(GL_FRONT, GL_SPECULAR, mat[3]["spc"])
		glMaterialfv(GL_FRONT, GL_SHININESS, mat[3]["shn"])
	else:
		glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[0]["dif"])
		glMaterialfv(GL_FRONT, GL_AMBIENT, mat[0]["amb"])
		glMaterialfv(GL_FRONT, GL_SPECULAR, mat[0]["spc"])
		glMaterialfv(GL_FRONT, GL_SHININESS, mat[0]["shn"])
	glutSolidSphere(8, 80, 80)
	glPopMatrix()
	glutSwapBuffers()

def main():
	init()
	glutDisplayFunc(display)
	glutKeyboardFunc(kb)
	glutMainLoop()

if __name__ == "__main__":
	main()