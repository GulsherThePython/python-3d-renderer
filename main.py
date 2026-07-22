import pygame
from draw import draw_wireframe
import draw
from rotate import rotate_along_z, rotate_along_x, rotate_along_y
from shapes import cube, cube_edges

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

vertices = cube(0, 0, 100, 10)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    draw_wireframe(screen, vertices, 60, 400, cube_edges())

    pygame.display.flip()
    clock.tick(60)