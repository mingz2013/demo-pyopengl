from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def drawFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    #glRotatef(1, 0, 1, 0)
    glutWireTeapot(0.5)
    # glutWireCube(1)
    # glutWireOctahedron()
    # glutWireSierpinskiSponge(0.1)
    # glutSolidTeapot(0.5)
    # glutSolidTorus(0.5, 0.5, 5, 10)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400, 400)
glutCreateWindow("First")
glutDisplayFunc(drawFunc)
#glutIdleFunc(drawFunc)
glutMainLoop()
