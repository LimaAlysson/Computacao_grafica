import pygame 
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import sys

class Base(object):

    def __init__(self, tamanhoTela=[1024, 1024]):
        pygame.init()