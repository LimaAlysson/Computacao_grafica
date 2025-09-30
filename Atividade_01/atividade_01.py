# Atividade 01 - Computação Gráfica
# Alysson José de Lima Bezerra

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
        pygame.display.set_caption("Atividade 01 - Computação Gráfica - Alysson José")
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
            glClearColor(1, 1, 1, 1)
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


class Circulo(Forma):
    
    def __init__(self, xc, yc, r, cor):
        super().__init__(cor)
        self.xc = xc
        self.yc = yc
        self.r = r
    
    def desenhar_ponto(self, x, y):
        glColor3f(self.cor[0], self.cor[1], self.cor[2])
        glBegin(GL_POINTS)
        glVertex2i(int(x), int(y))
        glEnd()
    
    def desenhar_pontos(self, x, y):
        self.desenhar_ponto(self.xc + x, self.yc + y)
        self.desenhar_ponto(self.xc - x, self.yc + y)
        self.desenhar_ponto(self.xc + x, self.yc - y)
        self.desenhar_ponto(self.xc - x, self.yc - y)
        self.desenhar_ponto(self.xc + y, self.yc + x)
        self.desenhar_ponto(self.xc - y, self.yc + x)
        self.desenhar_ponto(self.xc + y, self.yc - x)
        self.desenhar_ponto(self.xc - y, self.yc - x)


class CirculoCoordPolares(Circulo):

    def draw(self):
        delta_theta = 1.0 / self.r
        theta = 0.0

        while theta <= math.pi / 4.0:
            x = self.r * math.cos(theta)
            y = self.r * math.sin(theta)

            self.desenhar_pontos(round(x), round(y))

            theta += delta_theta


class CirculoPontosMedios(Circulo):

    def draw(self):
        R = int(self.r)
        x = 0
        y = R
        P = 1 - R
        self.desenhar_pontos(x, y)

        while x < y:
            x += 1

            if P < 0:
                P = P + 2 * x + 1
            else:
                y -= 1
                P = P + 2 * (x - y) + 1
            self.desenhar_pontos(x, y)


class Desenho(App):
    def initialize(self):
        self.circulo_polar = CirculoCoordPolares(300, 600, 150, cor=(1.0, 0.0, 0.0))
        self.circulo_pontos_medios = CirculoPontosMedios(700, 600, 150, cor=(0.0, 1.0, 0.0))
    
    def update(self):
        self.circulo_polar.draw()
        self.circulo_pontos_medios.draw()
        glFlush()


if __name__ == '__main__':
    # myApp = App()
    # myApp.run()
    d = Desenho()
    d.run()