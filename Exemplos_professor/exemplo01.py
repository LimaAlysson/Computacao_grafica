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
      self.vertices = [[0, 1, 0], 
                [-1, 0, 0],
                [1, 0, 0]]
      glLineWidth(10)

   def update(self):
      glBegin(GL_LINE_LOOP)
      for v in self.vertices:
          glVertex3fv(v)
      glEnd()
      
d = Desenho()
d.run()
