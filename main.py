import pygame
from draw import draw_points
from projection import project_points

pygame.init()

screen = pygame.display.set_mode((400, 400))

x_points = [
    -50,  50,  50, -50,
    -50,  50,  50, -50
]

y_points = [
    -50, -50,  50,  50,
    -50, -50,  50,  50
]

z_points = [
    200, 200, 200, 200,
    300, 300, 300, 300
]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    draw_points(screen, x_points, y_points, z_points, 60, 400)
    pygame.display.flip()