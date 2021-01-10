'''
Description: 
Author: He Yuhang
Github: https://github.com/hyhhhhhhhh
Date: 2020-12-12 17:13:59
LastEditors: Box
LastEditTime: 2020-12-31 16:02:53
'''

# -*- coding: utf-8 -*-	
# -------------------------------------------	
#  旋转、缩放、改变视点和参考点	
# -------------------------------------------	
from OpenGL.GL import *	
from OpenGL.GLU import *	
from OpenGL.GLUT import *	
import numpy as np	

import time
from controller import  IS_PERSPECTIVE, VIEW	, EYE, LOOK_AT, EYE_UP	,SCALE_K ,WIN_H,WIN_W,mouseclick,mousemotion,keydown

from ogl.objloader import OBJ,MTL

table_file ="table.obj"
chair_file = "model_normalized.obj"
# fidr = "resource/models/"
fidr = "resource/modelSequence/horses/"
Horses = list()
display = 0
for i in range(117):
    horse = 'horses_'+str(i)+'.obj'
    Horses.append(OBJ(fidr,horse))

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
	
    global IS_PERSPECTIVE, VIEW	,display
	
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

    # while True:
    #     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)	
    Horses[display].create_gl_list()
    glCallList(Horses[display].gl_list)
        # print(display)
    display+=1
    display=display%117
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
    glutIdleFunc(draw)                  # 注册刷新函数
	
    # glutReshapeFunc(reshape)            # 注册响应窗口改变的函数reshape()	
	
    # glutMouseFunc(mouseclick)           # 注册响应鼠标点击的函数mouseclick()	
    # glutMotionFunc(mousemotion)         # 注册响应鼠标拖拽的函数mousemotion()	
    # glutKeyboardFunc(keydown)           # 注册键盘输入的函数keydown()	
    glutMainLoop()                      # 进入glut主循环 