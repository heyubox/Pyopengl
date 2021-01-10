'''
Description: 
Author: He Yuhang
Github: https://github.com/hyhhhhhhhh
Date: 2020-12-12 17:13:59
LastEditors: Box
LastEditTime: 2021-01-07 16:52:47
'''

# -*- coding: utf-8 -*-	
# -------------------------------------------	
#  旋转、缩放、改变视点和参考点	
# -------------------------------------------	
from OpenGL.GL import *	
from OpenGL.GLU import *	
from OpenGL.GLUT import *	
import numpy as np	

from controller import  IS_PERSPECTIVE, VIEW	, EYE, LOOK_AT, EYE_UP	,SCALE_K ,WIN_H,WIN_W,mouseclick,mousemotion,keydown

from ogl.objloader import OBJ,MTL

# table_file ="table.obj"
# chair_file = "model_normalized.obj"
# fidr = "resource/models/"

# table = OBJ(fidr,table_file,1)
# table.create_bbox()

# chair1 = OBJ(fidr,chair_file,2)
# chair1.create_bbox()

# chair2 = OBJ(fidr,chair_file,2)
# chair2.create_bbox()

# chair3 = OBJ(fidr,chair_file,2)
# chair3.create_bbox()

# chair4 = OBJ(fidr,chair_file,2)
# chair4.create_bbox()
	
	
	
	
                  	
	
	
def init():	
	
    glClearColor(1.0, 1.0, 0.6, 1.0) # 设置画布背景色。注意：这里必须是4个参数	
	
    glEnable(GL_DEPTH_TEST)          # 开启深度测试，实现遮挡关系	
	
    glDepthFunc(GL_LEQUAL)           # 设置深度测试函数（GL_LEQUAL只是选项之一）	
	
	
	
def draw():	
	
    global IS_PERSPECTIVE, VIEW	
	
    global EYE, LOOK_AT, EYE_UP	
	
    global SCALE_K	
	
    global WIN_W, WIN_H	
	
        	
	
    # 清除屏幕及深度缓存	
	
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)	
	
    	
	
    # 设置投影（透视投影）	
	
    glMatrixMode(GL_PROJECTION)	
	
    glLoadIdentity()	
	
    	
	
    if WIN_W > WIN_H:	
	
        if IS_PERSPECTIVE:	
	
            glFrustum(VIEW[0]*WIN_W/WIN_H, VIEW[1]*WIN_W/WIN_H, VIEW[2], VIEW[3], VIEW[4], VIEW[5])	
	
        else:	
	
            glOrtho(VIEW[0]*WIN_W/WIN_H, VIEW[1]*WIN_W/WIN_H, VIEW[2], VIEW[3], VIEW[4], VIEW[5])	
	
    else:	
	
        if IS_PERSPECTIVE:	
	
            glFrustum(VIEW[0], VIEW[1], VIEW[2]*WIN_H/WIN_W, VIEW[3]*WIN_H/WIN_W, VIEW[4], VIEW[5])	
	
        else:	
	
            glOrtho(VIEW[0], VIEW[1], VIEW[2]*WIN_H/WIN_W, VIEW[3]*WIN_H/WIN_W, VIEW[4], VIEW[5])	
	
        	
	
    # 设置模型视图	
	
    glMatrixMode(GL_MODELVIEW)	
	
    glLoadIdentity()	
	
        	
	
    # 几何变换	
	
    glScale(SCALE_K[0], SCALE_K[1], SCALE_K[2])	
	
        	
	
    # 设置视点	
	
    gluLookAt(	
	
        EYE[0], EYE[1], EYE[2], 	
	
        LOOK_AT[0], LOOK_AT[1], LOOK_AT[2],	
	
        EYE_UP[0], EYE_UP[1], EYE_UP[2]	
	
    )	
	
    	
	
    # 设置视口	
	
    glViewport(0, 0, WIN_W, WIN_H)	
    	
	
    # ---------------------------------------------------------------	
    glBegin(GL_LINES)                    # 开始绘制线段（世界坐标系）	
	
    	
	
    # 以红色绘制x轴	
	
    glColor4f(1.0, 0.0, 0.0, 1.0)        # 设置当前颜色为红色不透明	
	
    glVertex3f(-0.8, 0.0, 0.0)           # 设置x轴顶点（x轴负方向）	
	
    glVertex3f(0.8, 0.0, 0.0)            # 设置x轴顶点（x轴正方向）	
	
    	
	
    # 以绿色绘制y轴	
	
    glColor4f(0.0, 1.0, 0.0, 1.0)        # 设置当前颜色为绿色不透明	
	
    glVertex3f(0.0, -0.8, 0.0)           # 设置y轴顶点（y轴负方向）	
	
    glVertex3f(0.0, 0.8, 0.0)            # 设置y轴顶点（y轴正方向）	
	
    	
	
    # 以蓝色绘制z轴	
	
    glColor4f(0.0, 0.0, 1.0, 1.0)        # 设置当前颜色为蓝色不透明	
	
    glVertex3f(0.0, 0.0, -0.8)           # 设置z轴顶点（z轴负方向）	
	
    glVertex3f(0.0, 0.0, 0.8)            # 设置z轴顶点（z轴正方向）	
		
	
    glEnd()                              # 结束绘制



#     glBegin(GL_POLYGON);
# glVertex3f(x1, y1, z1);
# glVertex3f(x2, y2, z2);
# glVertex3f(x3, y3, z3);
# glVertex3f(x4, y4, z4);
# glEnd();


    glColor4f(0.0, 1.0, 0.0, 0.5)  
    # 绘制地面和墙面
    glPushMatrix()
    glTranslatef(0.5,0,0)
    glBegin(GL_LINE_LOOP)
    # glBegin(GL_POLYGON)
    glVertex3f(-2,0,-2)
    glVertex3f(2,0,2)
    glVertex3f(-2,0,2)
    glVertex3f(2,0,-2)
    
    
    
    glEnd()
    glPopMatrix()

    glColor4f(1.0, 0.0, 0.0, 0.5)  
    #墙面
    glPushMatrix()
    glTranslatef(-1.5,0,0)
    glBegin(GL_LINE_LOOP)
    # glBegin(GL_POLYGON)

    glVertex3f(0,0,-2)
    glVertex3f(0,2,2)
    glVertex3f(0,2,-2)
    
    glVertex3f(0,0,2)
    
    
    glEnd()
    glPopMatrix()

    glColor4f(1.0, 0.0, 0.0, 0.5)  
    #墙面
    glPushMatrix()
    glTranslatef(2.5,0,0)
    glBegin(GL_LINE_LOOP)
    # glBegin(GL_POLYGON)

    glVertex3f(0,0,-2)
    glVertex3f(0,2,2)
    glVertex3f(0,2,-2)
    
    glVertex3f(0,0,2)
    
    
    glEnd()
    glPopMatrix()


    glColor4f(0.0, 0.0, 1.0, 0.5)  
    #墙面
    glPushMatrix()
    glTranslatef(0.5,0,-2)
    glBegin(GL_LINE_LOOP)
    # glBegin(GL_POLYGON)
    glVertex3f(2,0,0)
    glVertex3f(2,2,0)
    glVertex3f(-2,0,0)
    glVertex3f(-2,2,0)
    glEnd()
    glPopMatrix()

    #墙面
    glPushMatrix()
    glTranslatef(0.5,0,2)
    glBegin(GL_LINE_LOOP)
    # glBegin(GL_POLYGON)

    glVertex3f(2,0,0) 
    glVertex3f(-2,2,0)
    glVertex3f(2,2,0)
    glVertex3f(-2,0,0)
   
    
    glEnd()
    glPopMatrix()

# ----------------------------------------------------------------
    # #绘制桌子
    	
    # glPushMatrix()
    # glTranslatef(0.5,0,0)	#x y z 轴方向位移
    # glTranslatef(0,-table.vmin[1],0)
    # glRotatef(-90,0,1,0)
    # glRotatef(-90,1,0,0)
    # # glutWireTeapot(0.5)

    

    # table.create_gl_list()
    # glCallList(table.gl_list)
    # glPopMatrix()

    # #绘制椅子
    # glPushMatrix()
    # glTranslatef(0,-chair1.vmin[1],0)
    # glRotatef(90,0,1,0)
    # glRotatef(-90,1,0,0)
    # chair1.create_gl_list()
    # glCallList(chair1.gl_list)

    # glPopMatrix()




    # #绘制椅子
    # glPushMatrix()
    # glTranslatef(0,-chair2.vmin[1],0)
    # glTranslatef(1,0,0)
    # glRotatef(-90,0,1,0)
    # glRotatef(-90,1,0,0)
    # chair2.create_gl_list()
    # glCallList(chair2.gl_list)

    # glPopMatrix()




    # #绘制椅子
    # glPushMatrix()
    # glTranslatef(0,-chair3.vmin[1],0)
    # glTranslatef(0.5,0,0)
    # glTranslatef(0,0,0.7)
    # glRotatef(180,0,1,0)
    # glRotatef(-90,1,0,0)
    # chair3.create_gl_list()
    # glCallList(chair3.gl_list)

    # glPopMatrix()




    # #绘制椅子
    # glPushMatrix()
    # glTranslatef(0,-chair4.vmin[1],0)
    # glTranslatef(0.5,0,0)
    # glTranslatef(0,0,-0.7)
    # # glRotatef(90,0,1,0)
    # glRotatef(-90,1,0,0)
    # chair4.create_gl_list()
    # glCallList(chair4.gl_list)

    # glPopMatrix()

# ---------------------------------------------------------------	
	
    glutSwapBuffers()                    # 切换缓冲区，以显示绘制内容	
def reshape(width, height):	
	
    global WIN_W, WIN_H	
	
    	
	
    WIN_W, WIN_H = width, height	
	
    glutPostRedisplay()	
	
    	

if __name__ == "__main__":	
	
    glutInit()	
    displayMode = GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH	
    glutInitDisplayMode(displayMode)	
	
    glutInitWindowSize(WIN_W, WIN_H)	
    glutInitWindowPosition(300, 200)	
    glutCreateWindow(b'Quidam Of OpenGL')	
   	
	
    init()                              # 初始化画布	
	
    glutDisplayFunc(draw)               # 注册回调函数draw()	
	
    glutReshapeFunc(reshape)            # 注册响应窗口改变的函数reshape()	
	
    glutMouseFunc(mouseclick)           # 注册响应鼠标点击的函数mouseclick()	
    glutMotionFunc(mousemotion)         # 注册响应鼠标拖拽的函数mousemotion()	
    glutKeyboardFunc(keydown)           # 注册键盘输入的函数keydown()	
    glutMainLoop()                      # 进入glut主循环 