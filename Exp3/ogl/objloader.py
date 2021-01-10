from . import *


from OpenGL.GL import *
from OpenGL.GL import shaders
from OpenGL.GLU import *


import numpy as np
import pygame, OpenGL


def MTL(fdir,filename):
    contents = {}
    mtl = None
    for line in open(fdir+filename, "r"):
        if line.startswith('#'): continue
        values = line.split()
        if not values: continue
        if values[0] == 'newmtl':
            mtl = contents[values[1]] = {}
        elif mtl is None:
            raise ValueError( "mtl file doesn't start with newmtl stmt" )
        elif values[0] == 'map_Kd':
            # load the texture referred to by this declaration
            mtl[values[0]] = values[1]
            surf = pygame.image.load(fdir+mtl['map_Kd'])
            image = pygame.image.tostring(surf, 'RGBA', 1)
            ix, iy = surf.get_rect().size
            texid = mtl['texture_Kd'] = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, texid)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,
                GL_LINEAR)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA,
                GL_UNSIGNED_BYTE, image)
        else:
            #mtl[values[0]] = map(float, values[1:])

            mtl[values[0]] = [ float(x) for x in values[1:4]]
    return contents

class OBJ:
    def __init__(self, fdir, filename, swapyz=False):
        """Loads a Wavefront OBJ file. """
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        self.mtl=None

        self.vmax=None
        self.vmin =None

        self.mtlf=None

        self.ifloadmtl = False

        material = None
        for line in open(fdir+filename, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                #v = map(float, values[1:4])
                v=[ float(x) for x in values[1:4]]
                if swapyz:
                    v = v[0], v[2], v[1]
                self.vertices.append(v)
            elif values[0] == 'vn':
                #v = map(float, values[1:4])
                v=[ float(x) for x in values[1:4]]
                if swapyz:
                    v = v[0], v[2], v[1]
                self.normals.append(v)
            elif values[0] == 'vt':
                v = [float(x) for x in values[1:3]]

                self.texcoords.append(v)
            elif values[0] in ('usemtl', 'usemat'):
                material = values[1]
            elif values[0] == 'mtllib':
                #print(values[1])
                #self.mtl = MTL(fdir,values[1])
                self.mtlf = [fdir,values[1]]
            elif values[0] == 'f':
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = v.split('/')
                    face.append(int(w[0]))
                    if len(w) >= 2 and len(w[1]) > 0:
                        texcoords.append(int(w[1]))
                    else:
                        texcoords.append(0)
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(int(w[2]))
                    else:
                        norms.append(0)
                self.faces.append((face, norms, texcoords, material))

    def create_bbox(self):
        # self.vertices is not None
        ps=np.array(self.vertices)
        self.vmin=ps.min(axis=0)
        self.vmax=ps.max(axis=0)

        self.bbox_center=(self.vmax+self.vmin)/2
        self.bbox_half_r=np.max(self.vmax-self.vmin)/2


    def create_gl_list(self):
        if self.mtlf is not None and not self.ifloadmtl:
            print(self.mtlf, "---")
            self.mtl = MTL( *self.mtlf )
            self.ifloadmtl = True

        self.gl_list = glGenLists(1)
        glNewList(self.gl_list, GL_COMPILE)
        # glEnable(GL_TEXTURE_2D)
        # glFrontFace(GL_CCW)
        #glCullFace(GL_BACK)
        #glEnable(GL_CULL_FACE)

        for face in self.faces:
            vertices, normals, texture_coords, material = face
            #注释则不加载材质
            
            if self.mtl:
                mtl = self.mtl[material]
                if 'texture_Kd' in mtl:
                # use diffuse texmap
                    glBindTexture(GL_TEXTURE_2D, mtl['texture_Kd'])
                else:
                # just use diffuse colour
                #print(mtl['Kd'],"----")
                    glColor(*mtl['Kd'])



            glBegin(GL_POLYGON)
            for i in range(len(vertices)):
                if normals[i] > 0:
                    glNormal3fv(self.normals[normals[i] - 1])
                if texture_coords[i] > 0:
                    glTexCoord2fv(self.texcoords[texture_coords[i] - 1])
                glVertex3fv(self.vertices[vertices[i] - 1])
            glEnd()
        glDisable(GL_TEXTURE_2D)
        glEndList()

