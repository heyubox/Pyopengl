'''
Description: 
Author: He Yuhang
Github: https:#github.com/hyhhhhhhhh
Date: 2020-12-22 11:40:34
LastEditors: Box
LastEditTime: 2021-01-09 14:02:36
'''
import sys

from OpenGL.GL import *

from OpenGL.GLUT import *

from OpenGL.GLU import *

from PIL import Image

import numpy as np

from ogl.objloader import OBJ, MTL

from ogl.light import setup_lighting

from controller import IS_PERSPECTIVE, VIEW, EYE, LOOK_AT, EYE_UP, SCALE_K, WIN_H, WIN_W, mouseclick, mousemotion, keydown

from nubs import BindNubs,THE_LIST



fidr = "resource/modelSequence/cactus/"
Cactus = list()
display = 0
for i in range(128):
    cactus = 'cactus_' + str(i) + '.obj'
    Cactus.append(OBJ(fidr, cactus))


class MyPyOpenGLTest:
    def __init__(self,
                 width=640,
                 height=480,
                 models=Cactus,
                 title='MyPyOpenGLTest'.encode()):

        glutInit(sys.argv)

        self.texture_id = [0, 0]

        glutInitDisplayMode(GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)

        glutInitWindowSize(width, height)

        self.window = glutCreateWindow(title)
        
        self.InitGL(width, height)

        self.models = models

        self.display_max = len(models)
        self.display_iter = 0

        glutDisplayFunc(self.Draw)

        glutIdleFunc(self.Draw)
        
        glutMouseFunc(mouseclick)           # 注册响应鼠标点击的函数mouseclick()	
        
        glutMotionFunc(mousemotion)         # 注册响应鼠标拖拽的函数mousemotion()	
        
        glutKeyboardFunc(keydown)           # 注册键盘输入的函数keydown()	

        #绕各坐标轴旋转的角度

        self.x = 0.0

        self.y = 0.0

        self.z = 0.0

    #绘制图形

    def DrawModels(self):

        glPushMatrix()

        glEnable(GL_TEXTURE_2D)

        glBindTexture(GL_TEXTURE_2D, self.texture_id[0])

        self.models[self.display_iter].create_gl_list()

        glTranslatef(0,0.5,0)

        glRotate(-90,1,0,0)

        glCallList(self.models[self.display_iter].gl_list)

        self.display_iter += 1

        self.display_iter = self.display_iter % self.display_max

        glPopMatrix()

  
    def Draw(self):

        # 设置视点

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glLoadIdentity()

        glMatrixMode(GL_PROJECTION)

        glLoadIdentity()

        if WIN_W > WIN_H:

            if IS_PERSPECTIVE:

                glFrustum(VIEW[0] * WIN_W / WIN_H, VIEW[1] * WIN_W / WIN_H,
                          VIEW[2], VIEW[3], VIEW[4], VIEW[5])

            else:

                glOrtho(VIEW[0] * WIN_W / WIN_H, VIEW[1] * WIN_W / WIN_H,
                        VIEW[2], VIEW[3], VIEW[4], VIEW[5])

        else:

            if IS_PERSPECTIVE:

                glFrustum(VIEW[0], VIEW[1], VIEW[2] * WIN_H / WIN_W,
                          VIEW[3] * WIN_H / WIN_W, VIEW[4], VIEW[5])

            else:

                glOrtho(VIEW[0], VIEW[1], VIEW[2] * WIN_H / WIN_W,
                        VIEW[3] * WIN_H / WIN_W, VIEW[4], VIEW[5])

        # 设置模型视图

        glMatrixMode(GL_MODELVIEW)

        glLoadIdentity()

        glScale(SCALE_K[0], SCALE_K[1], SCALE_K[2])

        gluLookAt(EYE[0], EYE[1], EYE[2], LOOK_AT[0], LOOK_AT[1], LOOK_AT[2],
                  EYE_UP[0], EYE_UP[1], EYE_UP[2])

        glViewport(0, 0, WIN_W, WIN_H)

        #沿z轴平移

        # glTranslate(0.0, 0.0, -5.0)
        # self.DrawXyz()

        # self.DrawGround1()

        self.DrawSurface()

        self.DrawModels()

        #刷新屏幕，产生动画效果

        glutSwapBuffers()

        # 修改各坐标轴的旋转角度

    def DrawSurface(self):
        THE_LIST = BindNubs()
        # global THE_LIST
        glPushMatrix()
        glClear(GL_COLOR_BUFFER_BIT)
        # #切换纹理
        glEnable(GL_TEXTURE_2D)
        glColor3f(0, 0, 0)
        glBindTexture(GL_TEXTURE_2D, self.texture_id[1])

        glScale(0.2,0.2,0.2)
        glRotate(-90,1,0,0)
        glCallList(THE_LIST)
        
        glPopMatrix()

       

    def DrawGround1(self):

        glClear(GL_COLOR_BUFFER_BIT)
        # 切换纹理
        glEnable(GL_TEXTURE_2D)
        
        glColor3f(1, 5, 1)
        
        glBindTexture(GL_TEXTURE_2D, self.texture_id[0])
        
        glBegin(GL_POLYGON)
        
        glTexCoord2f(1.0, 1.0)

        glVertex3f(-1.0, -0., -1.0)

        glTexCoord2f(0.0, 1.0)

        glVertex3f(1.0, -0., -1.0)

        glTexCoord2f(0.0, 0.0)

        glVertex3f(1.0, -0., 1.0)

        glTexCoord2f(1.0, 0.0)

        glVertex3f(-1.0, -0., 1.0)

        glEnd()

    def DrawGround2(self):

        # #切换纹理

        glColor3f(1, 5, 1)

        glBindTexture(GL_TEXTURE_2D, self.texture_id[0])

        glBegin(GL_QUADS)

        glTexCoord2f(1.0, 1.0)

        glVertex3f(-1.0, -1.0, -1.5)

        glTexCoord2f(0.0, 1.0)

        glVertex3f(1.0, -1.0, -1.5)

        glTexCoord2f(0.0, 0.0)

        glVertex3f(1.0, -1.0, 1.0)

        glTexCoord2f(1.0, 0.0)

        glVertex3f(-1.0, -1.0, 1.0)

        glEnd()

    #加载纹理

    def LoadTexture(self):

        #载入纹理

        imgFiles = '1.jpg'

        img = Image.open(imgFiles)

        width, height = img.size

        img = img.tobytes('raw', 'RGBX', 0, -1)

        # 纹理索引为1

        self.texture_id[0] = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, self.texture_id[0])

        glTexImage2D(GL_TEXTURE_2D, 0, 4, width, height, 0, GL_RGBA,
                     GL_UNSIGNED_BYTE, img)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

        imgFiles = '2.jpg'

        img = Image.open(imgFiles)

        width, height = img.size

        img = img.tobytes('raw', 'RGBX', 0, -1)

        # 纹理索引为2

        self.texture_id[1] = glGenTextures(1)

        glBindTexture(GL_TEXTURE_2D, self.texture_id[1])

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA,
                     GL_UNSIGNED_BYTE, img)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR); # 线形滤波
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR); # 线形滤波

        # glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    def InitGL(self, width, height):

        self.LoadTexture()

        setup_lighting()

        glEnable(GL_TEXTURE_2D)

        glClearColor(0, 0, 0, 0.0)

        glClearDepth(1.0)

        glEnable(GL_TEXTURE_2D)

        glDisable( GL_CULL_FACE )

        glEnable(GL_DEPTH_TEST)  # 开启深度测试，实现遮挡关系

        glDepthFunc(GL_LEQUAL)  # 设置深度测试函数（GL_LEQUAL只是选项之一）

        glShadeModel(GL_SMOOTH)

        glEnable(GL_POINT_SMOOTH)

        glEnable(GL_LINE_SMOOTH)

        glEnable(GL_POLYGON_SMOOTH)

        glMatrixMode(GL_PROJECTION)

        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)

        glHint(GL_LINE_SMOOTH_HINT, GL_NICEST)

        glHint(GL_POLYGON_SMOOTH_HINT, GL_FASTEST)

        glLoadIdentity()

        gluPerspective(45.0, float(width) / float(height), 0.1, 100.0)

        glMatrixMode(GL_MODELVIEW)

    def MainLoop(self):

        glutMainLoop()


if __name__ == '__main__':

    w = MyPyOpenGLTest()

    w.MainLoop()