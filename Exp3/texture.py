'''
Description: 
Author: He Yuhang
Github: https://github.com/hyhhhhhhhh
Date: 2020-12-22 11:40:34
LastEditors: Box
LastEditTime: 2020-12-31 13:46:38
'''
import sys

from OpenGL.GL import *

from OpenGL.GLUT import *

from OpenGL.GLU import *

from PIL import Image

import numpy as np

WIN_W, WIN_H = 640, 480                             # 保存窗口宽度和高度的变量	

EYE = np.array([2.0, 2.0, 2.0])                     # 眼睛的位置（默认z轴的正方向）	
	
LOOK_AT = np.array([0.0, 0.0, 0.0])                 # 瞄准方向的参考点（默认在坐标原点）	
	
EYE_UP = np.array([0.0, 1.0, 0.0])                  # 定义对观察者而言的上方（默认y轴的正方向）	


class MyPyOpenGLTest:

    def __init__(self,

                 width=640,

                 height=480,

                 title='MyPyOpenGLTest'.encode()):

        glutInit(sys.argv)

        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

        glutInitWindowSize(width, height)

        self.window = glutCreateWindow(title)
        self.InitGL(width, height)
        
        glutDisplayFunc(self.Draw)

        glutIdleFunc(self.Draw)

        

        #绕各坐标轴旋转的角度

        self.x = 0.0

        self.y = 0.0

        self.z = 0.0



    #绘制图形

    def DrawXyz(self):
        glBegin(GL_LINES)                    # 开始绘制线段（世界坐标系）	
	
    	
        # glBindTexture(GL_TEXTURE_2D, 0)
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


        glClearColor(1.0, 1.0, 1.0, 0.0)

    def Draw(self):

            # 设置视点	
	


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()



        gluLookAt(	
	
            EYE[0], EYE[1], EYE[2], 	
	
            LOOK_AT[0], LOOK_AT[1], LOOK_AT[2],	
	
            EYE_UP[0], EYE_UP[1], EYE_UP[2]	
	
        )	

        glViewport(0, 0, WIN_W, WIN_H)

        #沿z轴平移

        # glTranslate(0.0, 0.0, -5.0)
        self.DrawXyz()

        self.DrawGround()

        #刷新屏幕，产生动画效果

        glutSwapBuffers()

        #修改各坐标轴的旋转角度

    def DrawGround(self):
        


        # #切换纹理

        glBindTexture(GL_TEXTURE_2D, 1)

        glBegin(GL_QUADS)        

        glTexCoord2f(1.0, 1.0)

        glVertex3f(-1.0, -1.0, -1.0)

        glTexCoord2f(0.0, 1.0)

        glVertex3f(1.0, -1.0, -1.0)

        glTexCoord2f(0.0, 0.0)

        glVertex3f(1.0, -1.0, 1.0)

        glTexCoord2f(1.0, 0.0)

        glVertex3f(-1.0, -1.0, 1.0)

        glEnd()


    #加载纹理

    def LoadTexture(self):

        #载入纹理

        imgFiles = ['1.jpg' for i in range(1,7)]



        img = Image.open(imgFiles[1])

        width, height = img.size

        img = img.tobytes('raw', 'RGBX', 0, -1)

        # 纹理索引为1

        glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, 1)

        glTexImage2D(GL_TEXTURE_2D, 0, 4,

                     width, height, 0, GL_RGBA,

                     GL_UNSIGNED_BYTE,img)

        glTexParameterf(GL_TEXTURE_2D,

                        GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        glTexEnvf(GL_TEXTURE_ENV,

                  GL_TEXTURE_ENV_MODE, GL_DECAL)

        

        

    def InitGL(self, width, height):

        self.LoadTexture()

        glEnable(GL_TEXTURE_2D)

        glClearColor(1.0, 1.0, 1.0, 0.0)

        glClearDepth(1.0)

        glDepthFunc(GL_LESS)

        glShadeModel(GL_SMOOTH)

        glEnable(GL_POINT_SMOOTH)

        glEnable(GL_LINE_SMOOTH)

        glEnable(GL_POLYGON_SMOOTH)

        glMatrixMode(GL_PROJECTION)

        glHint(GL_POINT_SMOOTH_HINT,GL_NICEST)

        glHint(GL_LINE_SMOOTH_HINT,GL_NICEST)

        glHint(GL_POLYGON_SMOOTH_HINT,GL_FASTEST)

        glLoadIdentity()

        gluPerspective(45.0, float(width)/float(height), 0.1, 100.0)

        glMatrixMode(GL_MODELVIEW)



    def MainLoop(self):

        glutMainLoop()



if __name__ == '__main__':

    w = MyPyOpenGLTest()

    w.MainLoop()