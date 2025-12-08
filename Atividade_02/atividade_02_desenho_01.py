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
        pygame.display.set_caption("Atividade 03 - Computação Gráfica - Alysson José")
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glScale(1, -1, 1)
        gluOrtho2D(0, 1024, 0, 1024)
        #glTranslatef(100.0, -50.0, 0.0)
        #glRotatef(45.0, 0.0, 0.0, 1.0) 
        #glScalef(1, 0.5, 2)
        self.clock = pygame.time.Clock()

    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        self.initialize()
        while True:
            self.input()
            glClearColor(0, 1, 0, 1)
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
        azul = 0, 0, 1
        vermelho = 1, 0, 0
        amarelo = 1, 1, 0
        preto = 0, 0, 0

        self.v1 = [[100, 100], [300, 100], [300, 300], [100, 300]]
        self.v2 = [[380, 100], [580, 100], [580, 300], [380, 300]]
        self.v3 = [[100, 380], [300, 380], [300, 580], [100, 580]]
        self.v4 = [[380, 380], [580, 380], [580, 580], [380, 580]]

        self.quadrado_azul = Quadrado(azul, self.v1, GL_QUADS)
        self.quadrado_vermelho = Quadrado(vermelho, self.v2, GL_QUADS)
        self.quadrado_amarelo = Quadrado(amarelo, self.v3, GL_QUADS)
        self.quadrado_preto = Quadrado(preto, self.v4, GL_QUADS)
    
    def update(self):

        glPushMatrix()
        glTranslatef(512, 512, 0)
        glRotatef(45, 0, 0, 1)
        glTranslatef(-340, -340, 0)

        glPointSize(10)
        glLineWidth(10)
        self.quadrado_azul.draw()
        self.quadrado_vermelho.draw()
        self.quadrado_amarelo.draw()
        self.quadrado_preto.draw()

        glPopMatrix()

if __name__ == '__main__':
    d = Desenho()
    d.run()