
import pygame
from OpenGL.GL import *

pygame.init()

W, H = 900, 600

screen = pygame.display.set_mode(
    (W, H),
    pygame.OPENGL | pygame.DOUBLEBUF
)

pygame.display.set_caption("THE ERROR - OPENGL")

# OpenGL setup
glViewport(0, 0, W, H)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, W, H, 0, -1, 1)

glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Button position
btn = pygame.Rect(100, 100, 200, 200)

# Initial color
green = False


# OpenGL button function
def draw_button():

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Blue or Green
    if green:
        glColor3f(0, 0.8, 0.2)
    else:
        glColor3f(0, 0, 0.8)

    # Button background
    glBegin(GL_QUADS)

    glVertex2f(btn.left, btn.top)
    glVertex2f(btn.right, btn.top)
    glVertex2f(btn.right, btn.bottom)
    glVertex2f(btn.left, btn.bottom)

    glEnd()

    # Border
    glLineWidth(5)

    if green:
        glColor3f(0, 0.3, 1)
    else:
        glColor3f(0, 0.9, 0.9)

    glBegin(GL_LINE_LOOP)

    glVertex2f(btn.left, btn.top)
    glVertex2f(btn.right, btn.top)
    glVertex2f(btn.right, btn.bottom)
    glVertex2f(btn.left, btn.bottom)

    glEnd()

    pygame.display.flip()


# Main loop
run = True

while run:

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            run = False

        if e.type == pygame.MOUSEBUTTONDOWN:

            if e.button == 1:

                if btn.collidepoint(e.pos):

                    green = not green

    draw_button()

pygame.quit()
