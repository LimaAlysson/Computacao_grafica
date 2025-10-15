import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

class App():
    def __init__(self, tamanhoTela=[1024, 1024]):
        pygame.init()
        self.tela = pygame.display.set_mode(tamanhoTela, pygame.DOUBLEBUF | pygame.OPENGL)
        pygame.display.set_caption("Atividade 02 - Computação Gráfica - Alysson José")
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glScale(1, -1, 1)
        gluOrtho2D(0, 1024, 0, 1024)
        self.clock = pygame.time.Clock()

    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        self.initialize()
        while True:
            self.input()
            glClearColor(1, 1, 0, 1)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
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

class Quadrado(Forma):

    def __init__(self, cor, pontos, primitiva):
        super().__init__(cor)
        self.pontos = pontos
        self.primitiva = primitiva
    

    def draw(self):
        glBegin(self.primitiva)

        glColor3d(self.cor[0], self.cor[1], self.cor[2])
        for p in self.pontos:
            glVertex2i(p[0], p[1])
        
        glEnd()

class Desenho(App):
    def initialize(self):
        vermelho = 1, 0, 0
        
        self.v1 = [[0, 500], [0, 524], [490, 524], [490, 500]]
        self.v2 = [[233, 233], [233, 780], [257, 780] ,[257, 233]]

        self.q1 = Quadrado(vermelho, self.v1, GL_QUADS)
        self.q2 = Quadrado(vermelho, self.v2, GL_QUADS)

    
    def update(self):

        glPushMatrix()
        glTranslatef(512, 512, 0)

        for i in range(4):
            glPushMatrix()
            angulo = i * 90
            glRotatef(angulo, 0, 0, 1)
            glTranslatef(-512, -512, 0)
            self.q1.draw()
            self.q2.draw()
            glPopMatrix()
        glPopMatrix()

if __name__ == '__main__':
    d = Desenho()
    d.run()