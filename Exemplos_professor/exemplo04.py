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
      pygame.display.set_caption("Aula 04 - Computação Gráfica")
      glMatrixMode( GL_PROJECTION )
      glLoadIdentity()
      glScale(1, -1, 1)
      gluOrtho2D( 0, 1024, 0, 1024)
      #glTranslatef(100, 500, 0)
      #glRotatef(10, 0, 0, 1)
      #glScalef(0.2,0.1, 0)
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
         pygame.time.wait(100)
         pygame.display.flip()
         
   def input(self):
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

class Forma:
   def __init__(self, color, points):
      self.color = color
      self.p = points
      
   def draw(self):
      glBegin(GL_QUADS)
      glColor3d(self.color[0], self.color[1], self.color[2])
      for p in self.p:
         glVertex2i(p[0], p[1])
      glEnd() 
       

class Desenho(Base):
   def cisalhamento(self, v, sx, sy):
      p = []
      for i in v:
         p.append([i[0] + sx*i[1], i[1] + sy*i[0]])
      return p
      
   def initialize(self):
      cor = 1, 1, 1
      self.v = [[100, 100], [500, 100], [500, 500], [100, 500]] 
      self.v = self.cisalhamento(self.v, 1, 0)
      self.forma = Forma(cor, self.v)

   def update(self):
      glLineWidth(10)
      self.forma.draw()
      
d = Desenho()
d.run()
