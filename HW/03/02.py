from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
TITLE = "CG: Homework #03-01 : Lighting positioning"
WIDTH, HEIGHT = 500, 500
view, theta = 0, 0
eye_x, eye_y, eye_z = 0, 0, 20
center_x, center_y, center_z = 0, 0, 0
ax, ay, az = 0, 1, 0
en_light = True

light = {
	"pos": [10, 10, 10, 0],
	"dif": [1.0, 1.0, 1.0, 1.0],
	"amb": [0.8, 0.8, 0.8, 1.0],
	"spc": [1.0, 1.0, 1.0, 1.0]
}

mat = [
	{#cylinder
		"dif": [1.0, 1.0, 0.0, 0.5],
		"amb": [0.8, 0.8, 0.0, 0.5],
		"spc": [1.0, 1.0, 0.8, 0.5],
		"shn": 10
	},{#sphere
		"dif": [1.0, 0.0, 0.0, 0.5],
		"amb": [0.8, 0.0, 0.0, 0.5],
		"spc": [1.0, 0.6, 0.6, 0.5],
		"shn": 10
	}
]

def init():
	glutInit()
	glutInitWindowSize(WIDTH, HEIGHT)
	glutInitWindowPosition(800, 50)
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
	glutCreateWindow(TITLE)
	glClearColor(0.1, 0.1, 0.1, 1.0)
	glShadeModel(GL_SMOOTH)
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glLightfv(GL_LIGHT0, GL_DIFFUSE, light["dif"])
	glLightfv(GL_LIGHT0, GL_AMBIENT, light["amb"])
	glLightfv(GL_LIGHT0, GL_SPECULAR, light["spc"])

def kb(key, x, y):
	global view, en_light, eye_x, eye_y, eye_z, ax, ay, az
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
	elif key == b'5':
		eye_x, eye_y, eye_z = 0, 0, 20
		ax, ay, az = 0, 1, 0
		print("Front view")
	elif key == b'8':
		eye_x, eye_y, eye_z = 0, 20, 0
		ax, ay, az = 0, 0, 1
		print("Top view")
	elif key == b'2':
		eye_x, eye_y, eye_z = 0, -20, 0
		ax, ay, az = 0, 0, 1
		print("Bottom view")
	elif key == b'4':
		eye_x, eye_y, eye_z = -20, 0, 0
		ax, ay, az = 0, 1, 0
		print("Left side view")
	elif key == b'6':
		eye_x, eye_y, eye_z = 20, 0, 0
		ax, ay, az = 0, 1, 0
		print("Right side view")
	glutPostRedisplay()


def setScene():
	glViewport(0, 0, WIDTH, HEIGHT)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	if view == 0:
		gluPerspective(90., 1., 1, 80)
	elif view == 1:
		glFrustum(-12, 12, -12, 12, 5, 80)
	else:
		glOrtho(-22, 22, -22, 22, 5, 80)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(eye_x, eye_y, eye_z, center_x, center_y, center_z, ax, ay, az)
	if en_light:
		glEnable(GL_LIGHTING)
	else:
		glDisable(GL_LIGHTING)
	glPushMatrix()
	# glRotatef(theta, 0, 1, 0)
	glLightfv(GL_LIGHT0, GL_POSITION, light["pos"])
	glPopMatrix()

def idle():
	global theta
	if theta == 360: 
		theta = 1
	else:
		theta += 1
	glutPostRedisplay()

def drawCylinder():
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[0]["dif"])
	glMaterialfv(GL_FRONT, GL_AMBIENT, mat[0]["amb"])
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat[0]["spc"])
	glMaterialfv(GL_FRONT, GL_SHININESS, mat[0]["shn"])
	glColor4fv(mat[0]["dif"])
	glutSolidCylinder(5, 16, 80, 80)

def drawSphere():
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[1]["dif"])
	glMaterialfv(GL_FRONT, GL_AMBIENT, mat[1]["amb"])
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat[1]["spc"])
	glMaterialfv(GL_FRONT, GL_SHININESS, mat[1]["shn"])
	glColor4fv(mat[1]["dif"])
	glutSolidSphere(1, 80, 80)

def display():
	setScene()
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	glPushMatrix()
	glTranslatef(0, -8, 0)
	glRotatef(-90, 1, 0, 0)
	glPushMatrix()
	glRotatef(theta, 0, 0, 1)
	glTranslatef(3, 0, 8)
	drawSphere()
	glPopMatrix()
	drawCylinder()
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