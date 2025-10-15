import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import sys
import math

class Base(object):
   def __init__(self, tamanhoTela=[1024, 1024]):
      pygame.init()
      self.tela = pygame.display.set_mode(tamanhoTela, pygame.DOUBLEBUF | pygame.OPENGL )
      pygame.display.set_caption("Aula 05 - Computação Gráfica")
      glMatrixMode( GL_PROJECTION )
      glLoadIdentity()
      glScale(1, -1, 1)
      gluOrtho2D( 0, 1024, 0, 1024)
      self.clock = pygame.time.Clock()

   def initialize(self):
      pass

   def update(self):
      pass
   
   def run(self):
      self.initialize()
      while True:
         self.input()
         glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
         self.update()
         pygame.time.wait(2000)
         pygame.display.flip()
         
         
   
   def input(self):
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

class Forma:
   def __init__(self, color, points, primitivas):
      self.color = color
      self.p = points
      self.primitivas = primitivas
      self.pos = 0
      
   def draw(self):
      glBegin(self.primitivas[self.pos])
      glColor3d(self.color[0], self.color[1], self.color[2])
      for p in self.p:
         glVertex2i(p[0], p[1])
      glEnd() 
      self.pos = (self.pos + 1)%len(self.primitivas)

class Desenho(Base):
   def initialize(self):
      cor = 1, 1, 1
      self.v = [[500, 500], [100, 100], [200, 80], [300, 120], [400, 100], [510, 90], [620, 120]] 
      self.primitivas = [GL_POINTS, GL_LINES, GL_LINE_STRIP, GL_LINE_LOOP, GL_TRIANGLES, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_QUADS, GL_QUAD_STRIP, GL_POLYGON]
      self.forma = Forma(cor, self.v, self.primitivas)

   def update(self):
      glPointSize(10)
      glLineWidth(10)
      self.forma.draw()
      
d = Desenho()
d.run()
