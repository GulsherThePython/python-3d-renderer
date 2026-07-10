import pygame
from draw import draw_cube
from rotate import rotate_along_z, rotate_along_x, rotate_along_y
from shapes import cube

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

vertices = cube(0, 0, 10, 10)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    vertex1 = rotate_along_z(vertex1, 1)
    vertex2 = rotate_along_z(vertex2, 1)
    vertex3 = rotate_along_z(vertex3, 1)
    vertex4 = rotate_along_z(vertex4, 1)
    vertex5 = rotate_along_z(vertex5, 1)
    vertex6 = rotate_along_z(vertex6, 1)
    vertex7 = rotate_along_z(vertex7, 1)
    vertex8 = rotate_along_z(vertex8, 1)

    vertex1 = rotate_along_x(vertex1, 1)
    vertex2 = rotate_along_x(vertex2, 1)
    vertex3 = rotate_along_x(vertex3, 1)
    vertex4 = rotate_along_x(vertex4, 1)
    vertex5 = rotate_along_x(vertex5, 1)
    vertex6 = rotate_along_x(vertex6, 1)
    vertex7 = rotate_along_x(vertex7, 1)
    vertex8 = rotate_along_x(vertex8, 1)

    vertex1 = rotate_along_y(vertex1, 1)
    vertex2 = rotate_along_y(vertex2, 1)
    vertex3 = rotate_along_y(vertex3, 1)
    vertex4 = rotate_along_y(vertex4, 1)
    vertex5 = rotate_along_y(vertex5, 1)
    vertex6 = rotate_along_y(vertex6, 1)
    vertex7 = rotate_along_y(vertex7, 1)
    vertex8 = rotate_along_y(vertex8, 1)


    draw_cube(screen, vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7, vertex8, 60, 400)

    pygame.display.flip()
    clock.tick(60)