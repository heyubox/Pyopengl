'''
Description: 
Author: He Yuhang
Github: https://github.com/hyhhhhhhhh
Date: 2014-01-16 23:29:56
LastEditors: Box
LastEditTime: 2020-12-12 16:30:02
'''

# from common import plane

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from ogl.objloader import OBJ,MTL
import common

import sys

table_file ="table.obj"
chair_file = "model_normalized.obj"
fidr = "resource/models/"

table = OBJ(fidr,table_file,1)
table.create_bbox()

chair = OBJ(fidr,chair_file,2)
chair.create_bbox()

window = 0
sph = common.sphere(16,16,1)
camera = common.camera()
plane = common.plane(12,12,1.,1.)
def InitGL(width,height):
    glClearColor(0.1,0.1,0.5,0.1)
    glClearDepth(1.0)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0,float(width)/float(height),0.1,100.0)    
    camera.move(0.0,3.0,-5)    
    
def DrawGLScene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)   


    glPushMatrix()
    # glRotatef(180,0,0,0)#绕Y轴旋转金字塔


    
    chair.create_gl_list()
    glCallList(chair.gl_list)
    
    glPopMatrix()
    # s = [2 / table.bbox_half_r] * 3
    # glScale(*s)

    # t = -table.bbox_center
    # glTranslate(*t)

    

    glPushMatrix()
    glTranslatef(0,0.4,0);	#x y z 轴方向位移
    
    # glutWireTeapot(0.5)

    

    table.create_gl_list()
    glCallList(table.gl_list)
    glPopMatrix()

    camera.setLookat()
    plane.draw() 
    glTranslatef(-1.5,0.0,0.0)
    glBegin(GL_QUADS)                  
    glVertex3f(-1.0, 1.0, 0.0)          
    glVertex3f(1.0, 1.0, 0.0)           
    glVertex3f(1.0, -1.0, 0.0)          
    glVertex3f(-1.0, -1.0, 0.0)        
    glEnd()    
    glTranslatef(3.0, 0.0, 0.0)
    sph.draw()                         
    glutSwapBuffers()

def mouseButton( button, mode, x, y ):	
	if button == GLUT_RIGHT_BUTTON:
		camera.mouselocation = [x,y]

def ReSizeGLScene(Width, Height): 
    glViewport(0, 0, Width, Height)		
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    
def main():
    # global window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(640,400)
    # glutInitWindowPosition(800,400)
    # window = glutCreateWindow("opengl")
    glutCreateWindow(b'First')
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutMouseFunc( mouseButton )
    glutMotionFunc(camera.mouse)
    glutKeyboardFunc(camera.keypress)
    glutSpecialFunc(camera.keypress)
    InitGL(640, 480)
    glutMainLoop()

main()