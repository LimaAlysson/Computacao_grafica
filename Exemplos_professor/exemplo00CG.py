import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import sys

class Base(object):
   def __init__(self, tamanhoTela=[1024, 1024]):
      pygame.init()
      self.tela = pygame.display.set_mode(tamanhoTela, pygame.DOUBLEBUF | pygame.OPENGL )
      pygame.display.set_caption("Aula 01 - Computação Gráfica")
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
         pygame.display.flip()
         self.clock.tick(60)
   
   def input(self):
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

class Desenho(Base):
   def initialize(self):
      glLineWidth(10)
   
   def boca(self):
      glBegin(GL_LINE_STRIP)
      x = -0.3
      while x < 0:
          y = 2*x**2 + 0.5*x +0.3
          glVertex2f(x, y)
          x = x + 0.01
      glEnd()
   
   def olho(self, pos):
      glBegin(GL_LINE_LOOP)
      x = pos[0]
      aux = 0.01
      while x < pos[1]:
          y = pos[2] + aux
          glVertex2f(x, y)
          x = x + 0.01
          aux = aux + 0.01
      aux = 0.01
      while x > pos[0]:
          y = pos[2] - aux
          glVertex2f(x, y)
          x = x - 0.01
          aux = aux + 0.01
      glEnd()
      
   def nariz(self):
      glBegin(GL_LINE_STRIP)
      x = -0.1
      while x < 0:
          y = 3*x**2 + 0.5*x +0.5
          glVertex2f(x, y)
          x = x + 0.01
      glEnd()
      
   def rosto(self):
      glBegin(GL_LINE_STRIP)
      x = -0.7
      while x < 0.5:
          y = 2*x**2 + 0.5*x 
          glVertex2f(x, y)
          x = x + 0.01
      glEnd()
      
   def update(self):
      self.rosto()
      self.boca()
      self.nariz()
      self.olho([-0.5, -0.3, 0.7])
      self.olho([0.1, 0.3, 0.7])
d = Desenho()
d.run()
