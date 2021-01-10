'''
Description: 
Author: He Yuhang
Github: https://github.com/hyhhhhhhhh
Date: 2020-12-12 16:32:39
LastEditors: Box
LastEditTime: 2020-12-12 16:32:40
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from ogl.objloader import OBJ,MTL



table_file ="table.obj"
chair_file = "model_normalized.obj"
fidr = "resource/models/"

table = OBJ(fidr,table_file,1)
table.create_bbox()

chair = OBJ(fidr,chair_file,2)
chair.create_bbox()


def run():
    pass