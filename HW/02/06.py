from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import arccos, dot, cross, array, sqrt, pi
TITLE = "CG: Homework #02-06 : Rotate sphere around cylinder"
WIDTH, HEIGHT = 500, 500
view, en_light, fill = True, True, True
theta, eye_x = 0, 0
a, sph_loc, cyl_height, angle = 5, 0, 0, 0
rot = None

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
	},{#grid
		"dif": [1.0, 1.0, 1.0, 0.6],
		"amb": [0.8, 0.8, 0.8, 0.0],
		"spc": [1.0, 0.6, 0.6, 0.0],
		"shn": 0
	}
]

def init():
	glutInit()
	glutInitWindowSize(WIDTH, HEIGHT)
	glutInitWindowPosition(800, 5)
	glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
	glutCreateWindow(TITLE)
	glClearColor(0.8, 0.8, 0.8, 1.0)
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	glEnable(GL_DEPTH_TEST)
	glLightfv(GL_LIGHT0, GL_POSITION, light["pos"])
	glLightfv(GL_LIGHT0, GL_DIFFUSE, light["dif"])
	glLightfv(GL_LIGHT0, GL_AMBIENT, light["amb"])
	glLightfv(GL_LIGHT0, GL_SPECULAR, light["spc"])

def kb(key, x, y):
	global view, en_light, eye_x, a, fill
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
	elif key == b'p':
		a = int(input("New location (a, a, a) : "))
	elif key == b'f':
		fill = not fill
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
		gluPerspective(90., 1., 5, 40)
	else:
		glOrtho(-10, 10, -10, 10, 5, 40)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()
	gluLookAt(eye_x, 0, 20, eye_x, 0, -1, 0, 1, 0)
	if en_light:
		glEnable(GL_LIGHTING)
		glEnable(GL_LIGHT0)
	else:
		glDisable(GL_LIGHT0)
		glDisable(GL_LIGHTING)

def drawGrid(a):
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[2]["dif"])
	glMaterialfv(GL_FRONT, GL_AMBIENT, mat[2]["amb"])
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat[2]["spc"])
	glMaterialfv(GL_FRONT, GL_SHININESS, mat[2]["shn"])
	glColor4ub(200, 200, 200, 100)
	glBegin(GL_LINES)
	glVertex3f(-100, 0, 0)
	glVertex3f( 100, 0, 0)
	glVertex3f(0, -100, 0)
	glVertex3f(0,  100, 0)
	glVertex3f(0, 0, -100)
	glVertex3f(0, 0,  100)
	glEnd()
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[1]["dif"])
	glMaterialfv(GL_FRONT, GL_AMBIENT, mat[1]["amb"])
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat[1]["spc"])
	glMaterialfv(GL_FRONT, GL_SHININESS, mat[1]["shn"])
	glColor3ub(200, 000, 000)
	glBegin(GL_LINES)
	glVertex3f( 0, 0, 0)
	glVertex3f( a, a, a)
	glEnd()
			
def drawCylinder(height):
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[0]["dif"])
	glMaterialfv(GL_FRONT, GL_AMBIENT, mat[0]["amb"])
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat[0]["spc"])
	glMaterialfv(GL_FRONT, GL_SHININESS, mat[0]["shn"])
	glColor4ub(200, 200, 000, 150)
	if fill:
		glutSolidCylinder(1, height, 80, 80)
	else:
		glutWireCylinder(1, height, 15, 15)

def drawSphere():
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat[1]["dif"])
	glMaterialfv(GL_FRONT, GL_AMBIENT, mat[1]["amb"])
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat[1]["spc"])
	glMaterialfv(GL_FRONT, GL_SHININESS, mat[1]["shn"])
	glColor4ub(200, 000, 000, 150)
	if fill:
		glutSolidSphere(1, 80, 80)
	else:
		glutWireSphere(1, 15, 15)

def calc(a):
	"""
		Calculate angle to rotate and height of cylinder, position of sphere to be at half of cylinder height\n
		a = top point of cylinder (x, y, z) = (a, a, a)
	"""
	global rot, cyl_height, sph_loc, angle
	zv = array([0, 0, 1])
	av = array([a, a, a])
	cyl_height = sqrt(dot(av, av))
	sph_loc = cyl_height * 0.5
	angle = arccos(dot(zv, av) / cyl_height) * 180 / pi
	rot = cross(zv, av)

def display():
	calc(a)
	setScene()
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	drawGrid(a)
	glPushMatrix()
	glRotatef(angle, rot[0], rot[1], rot[2])
	drawCylinder(cyl_height)
	glRotatef(theta, 0, 0, 1)
	glTranslatef(3, 0, sph_loc)
	drawSphere()
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
	