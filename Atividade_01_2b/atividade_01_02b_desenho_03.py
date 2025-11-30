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
        pygame.display.set_caption("Atividade 01_02b Computação Gráfica - Toróide")

        self.clock = pygame.time.Clock()
        self.rotation_angle = 0.0

    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        self.initialize()
        while True:
            self.input()
            glClearColor(1, 1, 1, 1.0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            self.update()
            
            pygame.display.flip()
            self.clock.tick(60)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

class Forma():
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

class Torus(Forma):
    def __init__(self, color, R, r, stacks=30, slices=30):
        super().__init__(color)
        self.R = R 
        self.r = r 
        self.stacks = stacks 
        self.slices = slices 
        
    def draw(self):
        glBegin(GL_QUADS)
        for i in range(self.stacks):
            phi_1 = 2 * math.pi * i / self.stacks
            phi_2 = 2 * math.pi * (i + 1) / self.stacks
            cos_phi_1 = math.cos(phi_1)
            sin_phi_1 = math.sin(phi_1)
            cos_phi_2 = math.cos(phi_2)
            sin_phi_2 = math.sin(phi_2)
            for j in range(self.slices):
                theta_1 = 2 * math.pi * j / self.slices
                theta_2 = 2 * math.pi * (j + 1) / self.slices
                cos_theta_1 = math.cos(theta_1)
                sin_theta_1 = math.sin(theta_1)
                cos_theta_2 = math.cos(theta_2)
                sin_theta_2 = math.sin(theta_2)
                x1 = (self.R + self.r * cos_phi_1) * cos_theta_1
                y1 = (self.R + self.r * cos_phi_1) * sin_theta_1
                z1 = self.r * sin_phi_1
                x2 = (self.R + self.r * cos_phi_1) * cos_theta_2
                y2 = (self.R + self.r * cos_phi_1) * sin_theta_2
                z2 = self.r * sin_phi_1
                x3 = (self.R + self.r * cos_phi_2) * cos_theta_2
                y3 = (self.R + self.r * cos_phi_2) * sin_theta_2
                z3 = self.r * sin_phi_2
                x4 = (self.R + self.r * cos_phi_2) * cos_theta_1
                y4 = (self.R + self.r * cos_phi_2) * sin_theta_1
                z4 = self.r * sin_phi_2

                color_index = (i + j) % 2
                if color_index == 0:
                    glColor3f(0.0, 0.0, 0.0) # Preto
                else:
                    glColor3f(1.0, 1.0, 1.0) # Branco
                glVertex3f(x1, y1, z1)
                glVertex3f(x2, y2, z2)
                glVertex3f(x3, y3, z3)
                glVertex3f(x4, y4, z4)

        glEnd()

class Desenho(App):
    def initialize(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (self.tela.get_width() / self.tela.get_height()), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, [0.0, 1.0, 3.0, 0.0]) 
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        self.torus = Torus([1.0, 0.5, 0.0], R=3.0, r=1.0)
        
    def update(self):
        glLoadIdentity()
        gluLookAt(0, 0, -10, 0, 0, 0, 0, 1, 0)
        self.torus.draw()
        

if __name__ == '__main__':
    d = Desenho()
    d.run()