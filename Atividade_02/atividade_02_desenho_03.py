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
        self.clock = pygame.time.Clock()

    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        self.initialize()
        while True:
            self.input()
            glClearColor(0, 0, 0, 1)
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

class Poligono(Forma):

    def __init__(self, cor, pontos, primitiva):
        super().__init__(cor)
        self.pontos = pontos
        self.primitiva = primitiva
    

    def draw(self):
        glBegin(self.primitiva)
        for i in range(len(self.pontos)):
            glColor3d(self.cor[i][0], self.cor[i][1], self.cor[i][2])
            glVertex2f(self.pontos[i][0], self.pontos[i][1])
        glEnd()

class Desenho(App):

    def initialize(self):
        gradiente = [[0, 1, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1], [1, 0, 0], [1, 0, 0]]
        self.v1 = [[512, 256], [612, 512], [768, 768], [512, 640], [256, 768], [412, 512]]   
        self.p1 = Poligono(gradiente, self.v1, GL_LINE_LOOP)
        
    def update(self):
        glPointSize(10)
        glLineWidth(10)
        self.p1.draw()
        

if __name__ == '__main__':
    d = Desenho()
    d.run()