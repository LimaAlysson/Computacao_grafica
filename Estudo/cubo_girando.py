import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    ( 1, -1, -1), # 0
    ( 1,  1, -1), # 1
    (-1,  1, -1), # 2
    (-1, -1, -1), # 3
    ( 1, -1,  1), # 4
    ( 1,  1,  1), # 5
    (-1, -1,  1), # 6
    (-1,  1,  1)  # 7
)

edges = (
    (0,1), (0,3), (0,4),
    (2,1), (2,3), (2,7),
    (6,3), (6,4), (6,7),
    (5,1), (5,4), (5,7)
)

colors = (
    (1,0,0), # Vermelho
    (0,1,0), # Verde
    (0,0,1), # Azul
    (1,1,0), # Amarelo
    (0,1,1), # Ciano
    (1,0,1)  # Magenta
)

### EXEMPLO DE CUBO GIRANDO

def main():
    pygame.init()

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_scene()
        pygame.display.flip()
        pygame.time.wait(10)


def Cube():
    glBegin(GL_LINES)

    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    
    glColor3fv((0,1,0)) 
    
    glEnd()


def draw_scene():
    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    Cube()

if __name__ == '__main__':
    main()