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
         #self.clock.tick(60)
         pygame.time.wait(300)
   
   def input(self):
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

class Desenho(Base):
   def initialize(self):
      self.vertices0 = [[0, 1, 0], 
                [-1, 0, 0],
                [1, 0, 0]]
      self.vertices1 = [[0, 1, 0], 
                [-1, 0, 0],
                [0, -1, 0]]
      self.vertices2 = [[0, -1, 0], 
                [-1, 0, 0],
                [1, 0, 0]]
      self.vertices3 = [[0, -1, 0], 
                [1, 0, 0],
                [0, 1, 0]]
      glLineWidth(10)
      self.numMagico = 0

   def update(self):
      glBegin(GL_LINE_LOOP)
      if self.numMagico == 0:
         aux = self.vertices0
      elif self.numMagico == 1:
         aux = self.vertices1
      elif self.numMagico == 2:
         aux = self.vertices2
      elif self.numMagico == 3:
         aux = self.vertices3
      self.numMagico = (self.numMagico + 1)%4
      for v in aux:
          glVertex3fv(v)
      glEnd()
      
d = Desenho()
d.run()
