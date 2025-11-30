import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

class App():
    def __init__(self, tamanhoTela=[1024, 768]):
        pygame.init()
        self.tela = pygame.display.set_mode(tamanhoTela, pygame.DOUBLEBUF | pygame.OPENGL)
        pygame.display.set_caption("Atividade 01_02b Computação Gráfica - Alysson José")
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (tamanhoTela[0]/tamanhoTela[1]), 0.1, 50.0)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        self.clock = pygame.time.Clock()

    def initialize(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE) 
        glCullFace(GL_BACK)

    def update(self):
        pass

    def run(self):
        self.initialize()
        while True:
            self.input()
            glClearColor(0.1, 0.1, 0.2, 1) 
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glLoadIdentity() 
            glTranslatef(0.0, 0.0, -8) 
            
            self.update()
            pygame.display.flip()
            self.clock.tick(60)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


class Forma():
    def __init__(self, cor):
        self.cor = cor

    def draw(self):
        pass

class Paralelepipedo(Forma):
    def __init__(self, cor, p1, p2):
        super().__init__(cor)
        self.p1 = p1
        self.p2 = p2
        self.vertices = self._generate_vertices(p1, p2) 
        self.faces = [
            (0, 3, 2, 1), 
            (4, 5, 6, 7), 
            (0, 4, 7, 3), 
            (1, 2, 6, 5), 
            (0, 1, 5, 4), 
            (3, 7, 6, 2)  
        ]
        self.face_colors = [
            [1.0, 0.0, 0.0], 
            [0.0, 0.0, 1.0], 
            [1.0, 1.0, 0.0],  
            [1.0, 0.0, 1.0], 
            [0.0, 1.0, 0.0], 
            [0.0, 1.0, 1.0], 
        ]

    def _generate_vertices(self, p1, p2):
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        
        vertices = [
            (x1, y1, z1),
            (x2, y1, z1),
            (x2, y2, z1), 
            (x1, y2, z1),
            
            (x1, y1, z2), 
            (x2, y1, z2),
            (x2, y2, z2), 
            (x1, y2, z2),
        ]
        return vertices

    def draw(self):
        glBegin(GL_QUADS)
        
        for i, face in enumerate(self.faces):
            glColor3fv(self.face_colors[i])
            
            for vertex_index in face:
                glVertex3fv(self.vertices[vertex_index])
                
        glEnd()

class Desenho(App):
    def initialize(self):
        super().initialize()
        
        ponto1_min = [-2.0, -1.0, -1.0] 
        ponto2_max = [ 2.0,  1.0,  1.0] 
        
        self.paralelepipedo = Paralelepipedo([1.0, 1.0, 1.0], ponto1_min, ponto2_max)
        
        self.angle_x = 0.0
        self.angle_y = 0.0

    def update(self):
        self.angle_x += 1.1
        self.angle_y += 0.3
        
        glRotatef(self.angle_x, 1, 0, 0)
        glRotatef(self.angle_y, 0, 1, 0) 
        
        self.paralelepipedo.draw()
        

if __name__ == '__main__':
    d = Desenho()
    d.run()