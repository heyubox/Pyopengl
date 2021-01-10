'''
Description: 
Author: He Yuhang
Github: https://github.com/hyhhhhhhhh
Date: 2020-12-12 13:55:47
LastEditors: Box
LastEditTime: 2020-12-13 00:34:15
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from ogl.objloader import OBJ,MTL

import common

import sys
# from ObjLoad.objloader import OBJ,MTL

sph = common.sphere(16,16,1)
camera = common.camera()
plane = common.plane(12,12,1.,1.)

table_file ="table.obj"
chair_file = "model_normalized.obj"
fidr = "resource/models/"

table = OBJ(fidr,table_file,1)
table.create_bbox()

# chair = OBJ(fidr,chair_file,2)
# chair.create_bbox()
# chair.create_bbox()
global x,y,z
x = 0
y = 0
z = 0

class Draw:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def drawsth(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        # gluPerspective(60, 1, 0.1, 10000)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        #gluLookAt( eyex=0, eyey=0, eyez=100, centerx=0, centery=0, centerz=0, upx=0, upy=1, upz=0)
        # gluLookAt(0, 0, 800, 0, 0, 0, 0, 1, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)#//清除屏幕和深度缓存
        glLoadIdentity()#//重置当前的模型观察矩阵
 
        glRotatef(self.x+180,self.y,self.z,0)#绕Y轴旋转金字塔

        print(self.x)

        self.x+=5
        # self.y+=5
        # self.z+=5

        table.create_gl_list()

        # s = [2 / table.bbox_half_r] * 3
        # glScale(*s)

        # t = -table.bbox_center
        # glTranslate(*t)

        glCallList(table.gl_list)
        # glutWireTeapot(0.5)

        glFlush()



def drawTableFunc():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # gluPerspective(60, 1, 0.1, 10000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #gluLookAt( eyex=0, eyey=0, eyez=100, centerx=0, centery=0, centerz=0, upx=0, upy=1, upz=0)
    # gluLookAt(0, 0, 800, 0, 0, 0, 0, 1, 0)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)#//清除屏幕和深度缓存
    glLoadIdentity()#//重置当前的模型观察矩阵
 
    # glRotatef(180,0,0,0)#绕Y轴旋转金字塔


    
    table.create_gl_list()

    # s = [2 / table.bbox_half_r] * 3
    # glScale(*s)

    # t = -table.bbox_center
    # glTranslate(*t)

    glCallList(table.gl_list)
    # glutWireTeapot(0.5)
    
    glFlush()

def drawXYZ():
    glLineWidth(3.0)
    glColor3f(1.0, 0.0, 0.0)#画红色的x轴
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glEnd()
    glColor3f(0.0, 1.0, 0.0)#画绿色的y轴
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glEnd()
    glColor3f(0.0, 0.0, 1.0)#画蓝色的z轴
    glBegin(GL_LINES)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 1.0)
    glEnd()

def drawChairandTableFunc():
    # glViewport(0,0,1,0)
    # glMatrixMode(GL_PROJECTION)
    # glLoadIdentity()
    # glOrtho(-50.0,50.0,-50.0,50.0,-1.0,1.0)
    


    # gluPerspective(60, 1, 0.1, 10000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #gluLookAt( eyex=0, eyey=0, eyez=100, centerx=0, centery=0, centerz=0, upx=0, upy=1, upz=0)
    # gluLookAt(0, 0, 800, 0, 0, 0, 0, 1, 0)
    drawXYZ()

    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)#//清除屏幕和深度缓存
    glPushMatrix()
    # glRotatef(180,0,0,0)#绕Y轴旋转金字塔


#     glBegin(GL_POLYGON);
# glVertex3f(x1, y1, z1);
# glVertex3f(x2, y2, z2);
# glVertex3f(x3, y3, z3);
# glVertex3f(x4, y4, z4);
# glEnd();
    glBegin(GL_POLYGON)
    


    # chair.create_gl_list()
    # glCallList(chair.gl_list)
    
    glPopMatrix()
    # s = [2 / table.bbox_half_r] * 3
    # glScale(*s)

    # t = -table.bbox_center
    # glTranslate(*t)

    

    glPushMatrix()
    glTranslatef(0.5,0,0)	#x y z 轴方向位移
    glRotatef(-90,0,1,0)
    glRotatef(-90,1,0,0)
    # glutWireTeapot(0.5)

    

    table.create_gl_list()
    glCallList(table.gl_list)
    glPopMatrix()

    
    
    glutSwapBuffers()
    # glViewport(0,0,1,1)
	# glMatrixMode(GL_PROJECTION)
	# glLoadIdentity()
	# glOrtho(-50.0,50.0,-50.0,50.0,-1.0,1.0)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glOrtho(-1.0,1.0,-1.0,1.0,-1.0,1.0)
    gluLookAt (0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    






glutInit()
# chair.create_gl_list()

# paint = Draw()
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
glutInitWindowSize(800,800)

# glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 1000, 0)) # 指的是光的朝向


glutCreateWindow(b'First')
# gluPerspective(20, 0, 100, 10000)

glEnable(GL_DEPTH_TEST)
glClearColor(0,0,0,0.0)

    
# glMatrixMode(GL_MODELVIEW)#设置当前矩阵模式为视图模型矩阵
# glLoadIdentity()#设置视点的位置，视线的方向和相机的向上方向
# gluLookAt(0,0,0, 0,0,-1, 0,1,0)#该设置为默认设置
# glScalef(0.3,1.0,0.5)#产生比例变换，分别设置物体在x，y，z方向上缩放因子，根据需要自己可以设置
# glRotatef(45,1.0,1.0,1.0)#产生旋转变换，让物体绕（1，1，1）轴旋转45度

# glLoadIdentity()#//重置当前的模型观察矩阵
glutReshapeFunc(reshape)
# gluLookAt(0, 0,0, 0, 0, 0, 0, 0, 0)
glutDisplayFunc(drawChairandTableFunc)

# glutDisplayFunc(drawTableFunc)
glutMainLoop()