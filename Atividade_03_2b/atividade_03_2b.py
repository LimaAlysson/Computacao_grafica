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
        pygame.display.set_caption("Atividade 05 - Computação Gráfica - Alysson José")
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (tamanhoTela[0]/tamanhoTela[1]), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST) 
        self.clock = pygame.time.Clock()
        self.rot_x = 0
        self.rot_y = 0

    def run(self):
        self.initialize()
        while True:
            self.input()
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            glTranslatef(0.0, 0.0, -25.0)
            glRotatef(self.rot_x, 1, 0, 0)
            glRotatef(self.rot_y, 0, 1, 0)
            self.update()
            pygame.display.flip()
            self.clock.tick(60)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rot_y -= 2
        if keys[K_RIGHT]:
            self.rot_y += 2
        if keys[K_UP]:
            self.rot_x -= 2
        if keys[K_DOWN]:
            self.rot_x += 2
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

class Octree():
    def __init__(self, niveis=3):
        self.niveis = niveis

    def draw(self, x, y, z, tamanho, cor):
        d = tamanho / 2
        glColor3fv(cor)
        glBegin(GL_LINES)
        v = [
            (x-d, y-d, z-d), (x+d, y-d, z-d), (x+d, y+d, z-d), (x-d, y+d, z-d),(x-d, y-d, z+d), (x+d, y-d, z+d), (x+d, y+d, z+d), (x-d, y+d, z+d)]
        arestas = [
            (0,1), (1,2), (2,3), (3,0), (4,5), (5,6), (6,7), (7,4), (0,4), (1,5), (2,6), (3,7)]
        for aresta in arestas:
            glVertex3fv(v[aresta[0]])
            glVertex3fv(v[aresta[1]])
        glEnd()

    def dividir(self, x, y, z, tamanho, nivel):
        if nivel < 0: return
        cor = [1,0,0]
        self.draw(x, y, z, tamanho, cor)
        if nivel > 0:
            novo_tamanho = tamanho / 2
            offset = tamanho / 4
            for i in [-1, 1]:
                for j in [-1, 1]:
                    for k in [-1, 1]:
                        self.dividir(x + i*offset, y + j*offset, z + k*offset, novo_tamanho, nivel - 1)

class Desenho(App):
    def initialize(self):
        self.octree = Octree(niveis=3)
        
    def update(self):
        glLineWidth(1)
        self.octree.dividir(0, 0, 0, 10.0, self.octree.niveis)

if __name__ == '__main__':
    d = Desenho()
    d.run()