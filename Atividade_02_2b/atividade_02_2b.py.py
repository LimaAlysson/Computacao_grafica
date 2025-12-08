import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
import math

class App():
    def __init__(self, tamanhoTela=[1024, 1024]):
        pygame.init()
        self.tela = pygame.display.set_mode(tamanhoTela, pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)
        pygame.display.set_caption("Atividade 04 - Computação Gráfica - Alysson José")
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (tamanhoTela[0]/tamanhoTela[1]), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)
        self.clock = pygame.time.Clock()
        self.angulo = 0

    def run(self):
        self.initialize()
        while True:
            self.input()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            glTranslatef(0.0, -1.5, -10.0) 
            glRotatef(self.angulo, 0, 1, 0)
            self.update()
            self.angulo += 1 
            pygame.display.flip()
            self.clock.tick(60)

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == VIDEORESIZE:
                glViewport(0, 0, event.w, event.h)

    def initialize(self):
        pass

    def update(self):
        pass

class Cone():
    def __init__(self, raio_b, altura, fatias):
        self.raio_b = raio_b
        self.altura = altura
        self.fatias = fatias

    def draw(self):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0, 0, 1) 
        glVertex3f(0, 0, 0)
        for i in range(self.fatias + 1):
            angulo = 2 * math.pi * i / self.fatias
            x = self.raio_b * math.cos(angulo)
            z = self.raio_b * math.sin(angulo)
            glVertex3f(x, self.altura, z) 
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.3, 0.7)
        for i in range(self.fatias):
            angulo = 2 * math.pi * i / self.fatias
            glVertex3f(self.raio_b * math.cos(angulo), self.altura, self.raio_b * math.sin(angulo))
        glEnd()

class Desenho(App):
    def initialize(self):
        self.cone = Cone(raio_b=2, altura=3, fatias=128)
        
    def update(self):
        self.cone.draw()

if __name__ == '__main__':
    d = Desenho()
    d.run()