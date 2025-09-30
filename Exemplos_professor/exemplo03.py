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
      pygame.display.set_caption("Aula 03 - Computação Gráfica")
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

class Forma:
   def __init__(self, color):
      self.color = color
      
   def draw(self):
      pass
      
   def round(self, num):
      return int(num+0.5)

class Reta(Forma):
   def __init__(self, p1, p2, color):
      super().__init__(color)
      self.p1 = p1
      self.p2 = p2
      
   def getReta(self):
      pass
   
   def draw(self):
      glBegin(GL_POINTS)
      glColor3d(self.color[0], self.color[1], self.color[2])
      for p in self.getReta():
         glVertex2i(p[0], p[1])
      glEnd() 
      
class RetaDDA(Reta):   
   def getReta(self):
      points = []
      step = abs(self.p1[0] - self.p2[0]) #dx
      if abs(self.p1[1] - self.p2[1]) > step:
         step = abs(self.p1[1] - self.p2[1]) #dy
      xInc = (self.p2[0] - self.p1[0])/step
      yInc = (self.p2[1] - self.p1[1])/step
      x = self.p1[0]
      y = self.p1[1]
      while x < self.p2[0]:
         points.append((self.round(x), self.round(y)))
         x = x + xInc
         y = y + yInc
      return points


class RetaBresenham(Reta):
   def getReta(self):
      points = []
      x = self.p1[0]
      y = self.p1[1]
      dx = self.p2[0] - self.p1[0]
      dy = self.p2[1] - self.p1[1]
      p = 2*dy - dx 
      while x < self.p2[0]:
         points.append((x, y))
         if p < 0:
            p = p + 2*dy
         else:
            y = y + 1
            p = p + 2*dy - 2*dx
         x = x + 1
      return points

class Circulo(Forma):
   def __init__(self, xc, yc, r, color):
      super().__init__(color)
      self.xc = xc
      self.yc = yc
      self.r = r

class CirculoSimples(Circulo):    
   def draw(self):
      x = self.xc - self.r
      glBegin(GL_POINTS)
      glColor3d(self.color[0], self.color[1], self.color[2])
      while x <= self.xc + self.r:
         aux = math.sqrt(self.r**2 - (x - self.xc)**2)
         y1 = self.yc + aux
         y2 = self.yc - aux
         glVertex2i(self.round(x), self.round(y1))
         glVertex2i(self.round(x), self.round(y2))
         x = x + 1
      glEnd()
      y = self.yc - self.r
      glBegin(GL_POINTS)
      glColor3d(self.color[0], self.color[1], self.color[2])
      while y <= self.yc + self.r:
         aux = math.sqrt(self.r**2 - (y - self.yc)**2)
         x1 = self.xc + aux
         x2 = self.xc - aux
         glVertex2i(self.round(x1), self.round(y))
         glVertex2i(self.round(x2), self.round(y))
         y = y + 1
      glEnd()

class Desenho(Base):
   def initialize(self):
      cor = 0, 0, 0
      self.r1 = RetaDDA((780, 100), (800, 900), cor)
      self.r2 = RetaBresenham((100, 780), (900, 800), cor)
      self.c1 = CirculoSimples(400, 800, 200, cor)
      self.t1 = RetaDDA((100, 100), (900, 100), cor)
      self.t2 = RetaDDA((500, 500), (900, 100), cor)
      self.t3 = RetaDDA((100, 100), (500, 500), cor)

   def update(self):
      #self.t1.draw()
      #self.t2.draw()
      #self.t3.draw()
      #self.r1.draw()
      #self.r2.draw()
      self.c1.draw()
      
d = Desenho()
d.run()
