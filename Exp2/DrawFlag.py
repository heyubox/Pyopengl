'''
Description: 
Author: He Yuhang
Github: https://github.com/hyhhhhhhhh
Date: 2020-12-12 17:07:11
LastEditors: Box
LastEditTime: 2020-12-13 10:26:21
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math as ma

PI = 3.1415926536

def drawStar(cx,cy,mx,my):
    length = ma.sqrt((mx - cx)*(mx - cx) + (my - cy)*(my - cy))
    cos1 = ma.cos(PI*0.4)
    sin1 = ma.sin(PI*0.4)
    cos2 = (mx-cx)/length
    sin2 = (my-cy)/length
    cos3 = ma.cos(PI*0.2)
    sin3 = ma.sin(PI*0.2)
    length2 = length*cos1/cos3
    point = [[0]*2 for i in range(10)]

    point[0][0]=mx
    point[0][1]=my
    tmp_cos=None
    tmp_sin =None
    for i in range(1,5):
        tmp_cos = cos1*cos2 - sin1*sin2
        tmp_sin = sin1*cos2 + cos1*sin2
        point[2 * i][0] = cx + length*tmp_cos
        point[2 * i][1] = cy + length*tmp_sin
        cos2 = tmp_cos
        sin2 = tmp_sin


    cos2 = (mx - cx) / length
    sin2 = (my - cy) / length


    for i in range(5):
        if i == 0 :
            tmp_cos = cos2*cos3 - sin2*sin3
            tmp_sin = sin2*cos3 + cos2*sin3
        else :
            tmp_cos = cos1*cos2 - sin1*sin2
            tmp_sin = sin1*cos2 + cos1*sin2
        
        point[i * 2 + 1][0] = cx + length2*tmp_cos
        point[i * 2 + 1][1] = cy + length2*tmp_sin
        cos2 = tmp_cos
        sin2 = tmp_sin

    glColor4f(1, 1, 0,1)
 
    #绘制五个三角形  
    glBegin(GL_TRIANGLES)
    for i in range(5) :
        for j in range(1,4):
            glVertex2fv(point[(2 * i + j) % 10])
    glEnd()

    #绘制五边形  
    glBegin(GL_POLYGON)
    for i in range(5):
        glVertex2fv(point[2 * i + 1])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT);#清除颜色缓存
#绘制星星  
    
    
    
    glColor4f(1, 0, 0,1)
    #绘制红旗  
    glBegin(GL_QUADS)
    glVertex2f(-0.9, 0.6)
    glVertex2f(0.9, 0.6)
    glVertex2f(0.9, -0.6)
    glVertex2f(-0.9, -0.6)
    glEnd()
    drawStar(-0.60, 0.30, -0.78, 0.36)
    drawStar(-0.30, 0.48, -0.24, 0.48)
    drawStar(-0.18, 0.36, -0.24, 0.36)
    drawStar(-0.18, 0.18, -0.18, 0.24)
    drawStar(-0.30, 0.06, -0.24, 0.06)
    # 设置红色  
    glutSwapBuffers()#交换缓冲区  
    
    
glutInit()
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
glutInitWindowPosition(10,10)
glutInitWindowSize(400,400)
glutCreateWindow(b"flag")
glutDisplayFunc(display)
glutMainLoop()