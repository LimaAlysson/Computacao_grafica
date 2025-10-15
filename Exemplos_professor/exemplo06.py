import pygame
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import sys

class Base(object):
   def __init__(self, tamanhoTela=[1024, 1024]):
      pygame.init()
      self.tela = pygame.display.set_mode(tamanhoTela, pygame.DOUBLEBUF | pygame.OPENGL )
      pygame.display.set_caption("Aula 05 - Computação Gráfica")
      glMatrixMode( GL_PROJECTION )
      glLoadIdentity()
      gluOrtho2D( 0, 1024, 0, 1024)
      self.clock = pygame.time.Clock()
      self.aux = 1

   def initialize(self):
      pass

   def update(self):
      pass
   
   def run(self):
      self.initialize()
      aux = 100
      while True:
         self.input()
         glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
         #glMatrixMode( GL_PROJECTION )
         #glLoadIdentity()
         #gluOrtho2D( 0, 1024, 0, 1024)
         #glTranslate(0, aux, 0)
         #aux += 100
         self.update()
         pygame.display.flip()
         #pygame.time.wait(1000)
         self.clock.tick(60)
      pygame.quit()
      sys.exit()

   def input(self):
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

class Desenho(Base):
   def initialize(self):
      pass
   
   def update(self):
      self.desenhaFoguete()  
   
   def bico(self):
      glBegin(GL_TRIANGLES)
      glColor3f(0,1,0)
      glVertex2i(200, 800)
      glVertex2i(300, 1000)
      glVertex2i(400, 800)
      glEnd()      
      
   def corpo(self):
      glBegin(GL_QUADS)
      glColor3f(0,0,1)
      glVertex2i(200, 400)
      glVertex2i(400, 400)
      glVertex2i(400, 800)
      glVertex2i(200, 800)
      glEnd()
      
   def asaEsquerda(self):
      glBegin(GL_TRIANGLES)
      glColor3f(1,0,0)
      glVertex2i(100, 400)
      glVertex2i(200, 400)
      glVertex2i(200, 600)
      glEnd()

   def asaDireita(self):
      glBegin(GL_TRIANGLES)
      glColor3f(1,0,0)
      glVertex2i(400, 400)
      glVertex2i(500, 400)
      glVertex2i(400, 600)
      glEnd()
  
   def chao(self): 
      glBegin(GL_QUADS)
      glColor3f(120/256,64/256,8/256)
      glVertex2i(0, 0)
      glVertex2i(0, 400)
      glVertex2i(1024, 400)
      glVertex2i(1024, 0)
      glEnd()
      
   def desenhaFoguete(self):
      glClearColor(1.0, 1.0, 1.0, 1.0)
      glClear(GL_COLOR_BUFFER_BIT)
      glPushMatrix()
      glTranslate(0, self.aux, 0)
      self.bico()
      self.corpo()
      self.asaEsquerda()
      self.asaDireita()
      glPopMatrix()
      self.aux = self.aux+1
      self.chao()
      glFlush()

d = Desenho()
d.run()







