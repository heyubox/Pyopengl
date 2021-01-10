'''
Description: 
Author: He Yuhang
Github: https://github.com/hyhhhhhhhh
Date: 2020-12-17 17:53:45
LastEditors: Box
LastEditTime: 2021-01-07 19:45:09
'''
import numpy as np
import pygame, OpenGL
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT.freeglut import *
import numpy
'''
GLfloat ambient[] = {0.3f, 0.3f, 0.3f, 1.0f};  // 环境强度
GLfloat diffuse[] = {1.0f, 1.0f, 1.0f, 1.0f};  // 散射强度
GLfloat specular[] = {1.0f, 1.0f, 1.0f, 1.0f}; // 镜面强度

'''


def setup_lighting():

    c=[1.0,1.0,1.0]

    glColor3fv(c)

    mat_specular = numpy.array(( 1.0, 1.0, 1.0, 1.0 ),'f')
    mat_shininess = GLfloat( 100.0 )

    # mat_specular=[0.18, 0.18, 0.18, 0.18 ]

    # mat_shininess=[ 64 ]
    global_ambient=[ 0.3, 0.3, 0.3, 0.05 ]
    light0_ambient=[ 0, 0, 0, 0 ]
    #light0_ambient = [0.2, 0.2, 0.2, 0.2]
    #light0_diffuse=[ 0.85, 0.85, 0.8, 0.85 ]
    light0_diffuse=[ 0.35, 0.35, 0.6, 0.65 ]

    light1_diffuse=[-0.01, -0.01, -0.03, -0.03 ]
    #light0_specular=[ 0.85, 0.85, 0.85, 0.85 ]
    light0_specular = [0.25, 0.25, 0.25, 0.25]
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, mat_shininess)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light0_ambient)
    # glLightfv(GL_LIGHT0, GL_DIFFUSE, light0_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light0_specular)
    # glLightfv(GL_LIGHT1, GL_DIFFUSE, light1_diffuse)
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, global_ambient)
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 0, 100, 0))
    glLightfv(GL_LIGHT1, GL_POSITION, (0, -100,0 , 0))

    glLightModeli(GL_LIGHT_MODEL_LOCAL_VIEWER, GL_FALSE)
    glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_FALSE)
    
    glEnable(GL_LIGHTING) # 开灯
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHT1)
    # glDisable(GL_LIGHT1)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)
